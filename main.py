from dotenv import load_dotenv
import os
import streamlit as st
from groq import Groq
import tempfile
import sounddevice as sd
import numpy as np
import wavio
import threading
import time

# Load environment variables
load_dotenv()
os.environ['api_key'] = os.getenv('api_key')

# Initialize Groq client
client = Groq(api_key=os.environ['api_key'])

st.set_page_config(page_title="Voice to English Transcription", page_icon="🎙️", layout="centered")
st.title("🎙️ Live Voice to English Transcription")
st.caption("Speak freely — start and stop when you want. The system detects, transcribes, and translates into English.")

# Initialize session state
if "recording" not in st.session_state:
    st.session_state.recording = False
if "recorded_audio" not in st.session_state:
    st.session_state.recorded_audio = None

fs = 44100  # Sample rate


def record_audio(stop_flag, buffer_list):
    """Continuously record small chunks until stop_flag is cleared"""
    while stop_flag["recording"]:
        chunk = sd.rec(int(fs * 1), samplerate=fs, channels=1, dtype="int16")
        sd.wait()
        buffer_list.append(chunk.copy())
        time.sleep(0.05)


# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🎙️ Start Recording", disabled=st.session_state.recording):
        st.session_state.recording = True
        st.success("Recording started... Speak now.")

        stop_flag = {"recording": True}
        audio_buffer = []

        def run_thread():
            record_audio(stop_flag, audio_buffer)
            # Once finished, combine and save
            audio_data = np.concatenate(audio_buffer, axis=0)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                wavio.write(tmp_file.name, audio_data, fs, sampwidth=2)
                st.session_state.recorded_audio = tmp_file.name

        thread = threading.Thread(target=run_thread, daemon=True)
        thread.start()
        st.session_state.stop_flag = stop_flag

with col2:
    if st.button("⏹️ Stop Recording", disabled=not st.session_state.recording):
        st.session_state.recording = False
        if "stop_flag" in st.session_state:
            st.session_state.stop_flag["recording"] = False
        st.success("Recording stopped.")

# Once audio exists, transcribe automatically
if st.session_state.recorded_audio and not st.session_state.recording:
    tmp_path = st.session_state.recorded_audio
    st.session_state.recorded_audio = None  # prevent re-running repeatedly

    with open(tmp_path, "rb") as file:
        with st.spinner("Transcribing your voice..."):
            transcription = client.audio.transcriptions.create(
                file=("recorded_audio.wav", file.read()),
                model="whisper-large-v3",
                response_format="verbose_json",
                temperature=0,
            )

    detected_lang = transcription.language
    transcribed_text = transcription.text

    st.subheader("Detected Language")
    st.write(detected_lang or "Unknown")

    st.subheader("Original Transcription")
    st.text_area("Transcribed Text", transcribed_text, height=200)

    # --- Translate automatically ---
    if transcribed_text.strip():
        with st.spinner("Translating to English..."):
            translation = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {"role": "system", "content": "Translate the following text into English accurately."},
                    {"role": "user", "content": transcribed_text},
                ],
            )

        translated_text = translation.choices[0].message.content
        st.subheader("English Translation")
        st.text_area("Translated Text", translated_text, height=200)
    else:
        st.warning("No transcription text found. Please record again.")

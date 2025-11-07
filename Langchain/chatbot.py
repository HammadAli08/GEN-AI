import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['api_key'] = os.getenv('api_key')

chat = ChatGroq(model="openai/gpt-oss-20b", api_key=os.environ['api_key'], temperature=0)

st.set_page_config(page_title="Personalized AI with Conversational Memory", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #ffffff;
        color: #000000;
    }
    .main {
        background: transparent;
        padding: 2rem 10%;
    }
    h1 {
        text-align: center;
        font-weight: 700;
        font-size: 2em;
        margin-bottom: 1.5rem;
        color: #000000;
    }
    .chat-wrapper {
        display: flex;
        flex-direction: column;
        gap: 2.5rem;
        margin-bottom: 2rem;
    }
    .user-row, .ai-row {
        display: flex;
        width: 100%;
    }
    .user-row {
        justify-content: flex-end;
    }
    .ai-row {
        justify-content: flex-start;
    }
    .user-bubble, .ai-bubble {
        background: #f3f3f3;
        color: #000000;
        border-radius: 18px;
        padding: 1rem 1.2rem;
        max-width: 60%;
        font-size: 1.05rem;
        line-height: 1.5;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.title("💬 Personalized AI with Conversational Memory")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)

for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.markdown(f'<div class="user-row"><div class="user-bubble">{msg.content}</div></div>', unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f'<div class="ai-row"><div class="ai-bubble">{msg.content}</div></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.markdown(f'<div class="user-row"><div class="user-bubble">{user_input}</div></div>', unsafe_allow_html=True)

    with st.spinner("Thinking..."):
        response = chat.invoke(st.session_state.chat_history)

    st.session_state.chat_history.append(AIMessage(content=response.content))
    st.markdown(f'<div class="ai-row"><div class="ai-bubble">{response.content}</div></div>', unsafe_allow_html=True)

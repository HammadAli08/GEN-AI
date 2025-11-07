from typing import TypedDict
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
os.environ['api_key'] = os.getenv('api_key')

llm=ChatGroq(model="openai/gpt-oss-20b", api_key=os.environ['api_key'], temperature=0.3)

## Schema Definition using TypedDict
class MovieInfo(TypedDict):
    title: str
    directors: str
    release_year: int
    genre: str
    rating: float

structured_output_prompt = llm.with_structured_output(MovieInfo)

response=structured_output_prompt.invoke("Spider man 3 movie info")

print(response)  # This will print a dictionary with the structured movie information6 Weeks
 
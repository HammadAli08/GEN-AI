from typing import Optional,Literal
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
os.environ['api_key'] = os.getenv('api_key')
llm=ChatGroq(model="openai/gpt-oss-20b", api_key=os.environ['api_key'], temperature=0.3)

## Schema Definition using Pydantic
class MovieInfoModel(BaseModel):
    title: str = Field(..., description="The title of the movie")
    directors: str = Field(..., description="The director(s) of the movie")
    release_year: int = Field(..., description="The year the movie was released")
    genre: Literal['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance', 'Documentary'] = Field(..., description="The genre of the movie")
    rating: float = Field(..., ge=0.0, le=10.0, description="The movie rating on a scale from 0 to 10")
    
structured_output_prompt = llm.with_structured_output(MovieInfoModel)
response=structured_output_prompt.invoke("Mission Impossible")
print(response) 
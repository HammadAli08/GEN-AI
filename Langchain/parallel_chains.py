from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['api_key'] = os.getenv('api_key')
llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.environ['api_key'], temperature=0.3)

# Define prompt templates
prompt1 = PromptTemplate(
    template="Provide a brief summary of the Topic: {title}",
    input_variables=["title"]
)
prompt2 = PromptTemplate(
    template="Explain the text: {text}",
    input_variables=["text"]
)

# Updated prompt3 expects both outputs from the parallel step
prompt3 = PromptTemplate(
    template="What are the key takeaways from the summary: {summary} and the explanation: {explanation}",
    input_variables=["summary", "explanation"]
)

parser = StrOutputParser()

chain0 = RunnableParallel(
    {
        "summary": prompt1 | llm | parser,
        "explanation": prompt2 | llm | parser,
    }
)

chain1 = prompt3 | llm | parser

final_chain = chain0 | chain1

response = final_chain.invoke({
    "title": "Agentic AI",
    "text": "Agentic AI refers to artificial intelligence systems that possess the capability to act autonomously, make decisions, and pursue goals without human intervention..."
})

print(response)

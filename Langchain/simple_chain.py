from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()
os.environ['api_key'] = os.getenv('api_key')

llm=ChatGroq(model="openai/gpt-oss-20b", api_key=os.environ['api_key'], temperature=0.3)

# Define a prompt template
prompt=PromptTemplate(
    template="Provide a brief summary of the following book: {book_title}",
    input_variables=["book_title"]
)

# Create a chain by combining the prompt template with the LLM
parser=StrOutputParser()
book_summary_chain = prompt | llm | parser


# Invoke the chain with an input
response = book_summary_chain.invoke({"book_title": "To Kill a Mockingbird"})
print(response)  # This will print a brief summary of the book "To Kill a Mockingbird"

book_summary_chain.get_graph().print_ascii()
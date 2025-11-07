from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch,RunnableLambda
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
os.environ['api_key'] = os.getenv('api_key')

# Initialize the LLM
llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.environ['api_key'], temperature=0.3)

# Define prompt
prompt = PromptTemplate(
    template="Classify the sentiment of this review as either Positive or Negative:\n{review}",
    input_variables=["review"]
)

# Define parser
parser = StrOutputParser()

# Build chain
sentiment_chain = prompt | llm | parser

prompt2= PromptTemplate(
    template="Based on the postive sentiment give appropriate response:\n{review}",
    input_variables=["review"]
)

prompt3= PromptTemplate(
    template="Based on the negative sentiment give appropriate response:\n{review}",
    input_variables=["review"]
)

runnable_chain = RunnableBranch(
    (lambda x: x.strip().lower() == "positive", sentiment_chain | prompt2 | llm | parser),
    (lambda x: x.strip().lower() == "negative", sentiment_chain | prompt3 | llm | parser),
    RunnableLambda(lambda x: True, lambda x: "Sentiment could not be determined." )
)

final_chain = sentiment_chain | runnable_chain

# Example usage
review_text = "I absolutely hate this product! It has ruin my life for the worse."
response = final_chain.invoke({"review": review_text}) 

print(final_chain.get_graph().draw_ascii())
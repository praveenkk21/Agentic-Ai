from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOuptutParser

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.8
)

for chunk in model.stream("Write a four line about the python debugging"):
    print(chunk.content, end="", flush=True)
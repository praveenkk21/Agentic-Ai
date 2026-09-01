from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOuptutParser
from langchain_huggingface import ChatHuggingFace, HunggingFaceEndpoint

load_dotenv()

endpoint = HunggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text generator",
    max_new_token=200,
    temperature=0.3
)

model = ChatHuggingFace(llm=endpoint)
print(model.invoke("Explain what is Openweights model in two lines").content)
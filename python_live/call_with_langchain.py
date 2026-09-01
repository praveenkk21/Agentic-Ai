from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage(
        content="""
        You are a Python teacher.

        You ONLY answer questions related to Python programming.

        If the user asks about Java, C++, JavaScript, databases,
        or any other topic outside Python, do not answer the question.

        Instead, say:
        "Sorry, I can only answer Python-related questions."
        """
    ),

    HumanMessage(content="What is tuple in python?")
]

response = model.invoke(messages)

print(response.content)
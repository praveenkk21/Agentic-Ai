from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a {language}, Keep answe under {limit} words"
        ),
        (
            "human",
            "Explain {topic} to a beginner"
        )
    ]
)

filled = prompt.invoke({
    "language":"Python",
    "limit":80,
    "topic": "decorator"
})

response = model.invoke(filled)

print(response.content)
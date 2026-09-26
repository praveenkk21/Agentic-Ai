from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser
)

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.8
    )

prompt = ChatPromptTemplate.from_messages(
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

parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({
    "language" : "java",
    "limit"  : "5",
    "topic" : "callable"
}))
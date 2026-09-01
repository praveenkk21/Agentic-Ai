from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import {
    StrOuptutParser,
    JsonOutputParser
}

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=8
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

parser = StrOuptutParser()

chain = prompt | model | parser

print(chain.invoke({
    "language" : "java",
    "topic" : "callable"
}))
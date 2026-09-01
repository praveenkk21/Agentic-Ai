from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import {
    StrOuptutParser,
    JsonOutputParser
}
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI{
    model="gpt-40-mini"
    temperature=8
}

text_parser = StrOutputParser()

response = model.invoke("Name Three Python web framework")

print(text_parser.invoke(response))

json_parser = JsonOutputParser()

json_prompt = ChatPromptTemplate.from_messages([
    
        (
            "system",
            "reply with Json only"
        ),
        (
            "human",
            "Explain about the {topic} framework when created"
        )
])

filled = json_prompt.invoke([
    "topic": "FastApi"
])

raw_reply = model.invoke(filled)

data= model.invoke(raw_reply)

print(type(data))

print(data['name'], data['year'])
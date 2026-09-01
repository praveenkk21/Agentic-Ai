from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

image_url="https://wallpaperaccess.com/full/1101027.jpg"

url_message = HumanMessage(content=[
    {
        "type" : "text",
        "text" : "Describe this picture in one word"
    },
    {
        "type" : "image",
        "image_url": image_url
    }
])

response = model.invoke(url_message)

print(response.content)
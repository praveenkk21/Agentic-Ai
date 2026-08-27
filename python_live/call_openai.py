from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

def call_openai(prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return response.output_text

def main():
    result = call_openai("Explain Java HashMap in simple words")
    print(result)

if __name__ == "__main__":
    main()

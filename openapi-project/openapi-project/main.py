from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def call_openai(prompt):

    response = client.responses.create(
        model="gpt-5.6",
        input=prompt
    )

    return response.output_text



def main():
    # Call the method
    result = call_openai("Explain Java HashMap in simple words")

    print(result)


if __name__ == "__main__":
    main()

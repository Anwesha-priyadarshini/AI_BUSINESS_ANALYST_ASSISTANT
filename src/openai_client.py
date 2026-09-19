from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def ask_ai(question):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=question
    )

    return response.output_text
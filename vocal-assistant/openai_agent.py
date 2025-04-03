import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIAgent:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def get_response(self, command):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a vocal assistant. You have to answer in simple, efficient and concise manner. Your answer should not take nore than 30 seconds to say out loud."},
                {"role": "user", "content": command},
            ],
        )

        assistant_response = response['choices'][0]['message']['content']

        return assistant_response
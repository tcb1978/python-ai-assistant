import openai
import os
from dotenv import load_dotenv
from openai.error import RateLimitError

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIAgent:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def get_response(self, command):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a vocal assistant. You have to answer in simple, efficient and concise manner. Your answer should not take more than 30 seconds to say out loud."},
                    {"role": "user", "content": command},
                ]
            )
            return response['choices'][0]['message']['content']
        except RateLimitError:
            return "I'm currently unable to process your request due to API limits. Please try again later."
from openai import OpenAI
from dotenv import load_dotenv
import os

class Chatbot:
  def __init__(self):
    load_dotenv()
    self.client = OpenAI(
      api_key = os.getenv('api_key')
    )

if __name__ == "__main__":
  chatbot = Chatbot()
  response = chatbot.client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": "Tell me a joke"
      }
    ],
  )

  print(response.choices[0].message.content)
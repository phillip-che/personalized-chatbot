from openai import OpenAI
from dotenv import load_dotenv
import os

class Chatbot:

  def __init__(self):
    load_dotenv()
    self.messages = []
    self.client = OpenAI(
      api_key = os.getenv('api_key')
    )
    
  def get_response(self, message):
    self.messages.append({"role":"user", "content":message})
    response = chatbot.client.chat.completions.create(
      model = "gpt-3.5-turbo",
      messages = self.messages
    )
    reply = response.choices[0].message.content
    self.messages.append({"role":"system", "content":reply})

    return reply

if __name__ == "__main__":
  chatbot = Chatbot()
  bot_type = input("What type of chatbot would you like to create?\n")
  chatbot.messages.append({"role": "system", "content": bot_type})

  print(chatbot.get_response(input("Ask a question: ")))
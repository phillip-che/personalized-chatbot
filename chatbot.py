from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
import os

class Chatbot:

  def __init__(self):
    load_dotenv()
    self.messages = []
    self.client = OpenAI(
      api_key = os.getenv('api_key')
    )
    self.personality = ""
    
  def get_response(self, message, history):
    self.messages.append({"role":"user", "content":message})
    response = chatbot.client.chat.completions.create(
      model = "gpt-3.5-turbo",
      messages = self.messages,
      temperature=1.0,
      stream=True
    )
    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              yield partial_message

    self.messages.append({"role":"system", "content":partial_message})
    
    return partial_message
  
  def set_personality(self, personality):
    self.personality = personality
    chatbot.messages.append({"role": "system", "content": personality})

if __name__ == "__main__":
  chatbot = Chatbot()
  personality = input("What type of chatbot would you like to create?\n")
  chatbot.set_personality(personality)
  gr.ChatInterface(chatbot.get_response).launch()
  
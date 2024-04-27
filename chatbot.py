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
    print(personality)
    self.personality = personality
    chatbot.messages.append({"role": "system", "content": "Answer the question like you are a normal human feeling the following: " + personality + ". Ignore any previous submissions"})


if __name__ == "__main__":
  chatbot = Chatbot()
  chatbot.set_personality("Happy")
  with gr.Blocks(fill_height=True) as bot:
    with gr.Row():
      radio = gr.Radio(["Happy", "Sad", "Angry"], label="Moods", info="Please Select a Mood", value = "Happy")
      text = gr.Textbox(label="Moods",info="Enter your own mood",lines=1)
    interface = gr.ChatInterface(chatbot.get_response)
    text.submit(fn = chatbot.set_personality,inputs=[text], outputs = [text])
    radio.change(fn = chatbot.set_personality,inputs=[radio],outputs = None)
  bot.launch()
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')

client = OpenAI(
  api_key=DEEPSEEK_API_KEY,
  base_url='https://api.deepseek.com'
)

def completion(prompt, system_prompt='You are a helpful assistant.'):
  response = client.chat.completions.create(
    model='deepseek-chat',
    messages=[
      {'role':'system', 'content':system_prompt},
      {'role':'user', 'content':prompt}
    ],
    stream=False
  )
  ai_message = response.choices[0].message
  return ai_message.content

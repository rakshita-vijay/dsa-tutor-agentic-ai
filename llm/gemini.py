import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


my_llm = LLM(
  model = 'gemini/gemini-2.5-flash',
  api_key = api_key,
  temperature = 0.6,
  max_tokens = 1024
)

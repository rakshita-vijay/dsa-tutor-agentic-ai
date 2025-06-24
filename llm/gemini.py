import os
import google.generativeai as genai
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

def get_gemini_model():
  api_key = os.getenv("GEMINI_API_KEY")
  if not api_key:
      raise ValueError("GEMINI_API_KEY not found in .env")
  genai.configure(api_key=api_key)
  return genai.GenerativeModel("gemini-2.0-flash")

my_llm = LLM(
  model = 'gemini/gemini-2.0-flash',
  api_key = os.getenv("GEMINI_API_KEY"),
  temperature = 0.8,
  max_tokens = 2048
)

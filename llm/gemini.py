import os
import google.generativeai as genai 

def get_gemini_model():
  api_key = os.getenv("GEMINI_API_KEY")
  if not api_key:
      raise ValueError("GEMINI_API_KEY not found in .env")
  genai.configure(api_key=api_key)
  return genai.GenerativeModel("gemini-2.0-flash") 

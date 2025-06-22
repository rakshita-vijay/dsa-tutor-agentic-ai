from crewai import LLM

api_key = "AIzaSyDFO8_NWA5nV08fpZVOjZrdSUN8StjGnbk"

my_llm = LLM(
  model = 'gemini/gemini-2.5-flash',
  api_key = api_key,
  temperature = 0.6,
  max_tokens = 1024
)

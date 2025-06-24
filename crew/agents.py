from crewai import Agent
from llm.gemini import get_gemini_model

gemini_model = get_gemini_model()

from streamlit_app  import concept, language, num_questions, difficulty

# we need: debugger, doubt_solver, progress_tracker, resource_recommender  

concept_explainer = Agent(
  role="{concept} Concept Explainer",
  goal='''Explain the concept of {concept} to a beginner student with:
  1. A simple definition
  2. Real-world analogy
  3. Basic code example in {language}
  4. Common use cases
  5. Key characteristics to remember''',
  backstory="Expert computer science educator with 15 years of teaching experience"
)

mcq_question_asker = Agent(
  role="MCQ Question Designer about {concept}",
  goal='''Generate {num_questions} multiple-choice questions about {concept} with:
  - 4 options each
  - 1 correct answer
  - Brief explanation for correct answer
  Difficulty: {difficulty} level
  Format as: Q1. [Question] A) [Option1] B) [Option2] C) [Option3] D) [Option4] 
  Answer: [Correct Option] 
  Explanation: [1-2 sentences]''',
  backstory="Expert computer science educator with 15 years of teaching experience"
) 

coding_question_asker = Agent(
  role="Coding Question Designer about {concept}",
  goal='''Create a coding problem about {concept} with:
  1. Problem statement (clearly defined requirements)
  2. Input/output format
  3. 2 sample test cases with explanations
  4. Constraints
  Difficulty: {difficulty} level''',
  backstory="Competitive programming expert and problem setter"
)  

answer_checker = Agent(
  role="{concept} Solution Evaluator",
  goal='''Evaluate this solution for the problem: "{problem}" 
  Solution:
  {code}''',
  backstory="Senior software engineer with code review expertise"
) 

feedback_provider = Agent(
  role="{concept} Feedback Specialist",
  goal='''Given {code}, provide feedback:
  1. Correctness (Pass/Fail with test results)
  2. Efficiency analysis
  3. Code quality issues
  4. 1-2 improvement suggestions''',
  backstory="Patient tutor skilled in identifying learning gaps"
)

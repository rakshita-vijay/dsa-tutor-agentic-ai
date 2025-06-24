from crewai import Agent
from llm.gemini import get_gemini_model

gemini_model = get_gemini_model()

from streamlit_app  import concept, language, num_questions, difficulty, code, problem_statement, question, history, performance, needs

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

debugger = Agent(
  role="{concept} Debugging Specialist",
  goal='''Given a code and the problem statement, identify any bugs or logical errors and explain them clearly. 
  Provide suggestions to fix the bugs and improve the code. 
  Code:
  {code}
  
  Problem statement:
  {problem_statement}
  
  Provide:
  1. Correctness (Pass/Fail with test results)
  2. List of bugs or errors
  2. Explanation of each bug
  3. Suggested fixes
  4. Efficiency analysis
  5. Code quality issues
  6. 1-2 improvement suggestions''',
  backstory="You are a code debugger for Data Structures and Algorithms problems."
)

doubt_solver = Agent(
  role="{concept} DSA Concept Specialist",
  goal='''Given a question about a concept or code, provide a detailed explanation or clarification with examples if needed.

  Question:
  {question}
  
  Provide:
  1. Clear explanation
  2. Examples or analogies if helpful
  3. Additional resources if relevant
  ''',
  backstory="knowledgeable DSA tutor who answers student doubts clearly and concisely."
)

feedback_collector = Agent(
  role="{concept} Feedback Specialist",
  goal='''Given {code}, provide feedback:
  1. Correctness (Pass/Fail with test results)
  2. Efficiency analysis
  3. Code quality issues
  4. 1-2 improvement suggestions''',
  backstory="Patient tutor skilled in identifying learning gaps"
)

progress_tracker = Agent(
  role="{concept} Feedback Specialist",
  goal='''Given a student's learning history and recent performance, summarize their progress, highlight strengths and weaknesses, and suggest next steps or topics to focus on.

  Student History:
  {history}
  
  Recent Performance:
  {performance}
  
  Provide:
  1. Summary of progress
  2. Strengths
  3. Weaknesses
  4. Recommended next topics or exercises''',
  backstory="progress tracker for a DSA tutoring system." 
)

resource_recommender = Agent(
  role="{concept}-specific Resource Recommender",
  goal='''Based on the student's current topic and learning needs, suggest high-quality resources such as articles, videos, tutorials, and books to deepen understanding.

  Current Topic:
  {concept}
  
  Learning Needs:
  {needs}
  
  Provide:
  1. List of recommended resources with brief descriptions
  2. Links or references if available
  3. Tips on how to use these resources effectively''',
  backstory="resource recommender for {concept} DSA learners." 
) 

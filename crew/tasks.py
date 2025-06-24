from crewai import Task

# Import the dynamic agent creation functions
from crew.agents import get_concept_explainer, get_mcq_question_asker, get_coding_question_asker, get_answer_checker, get_debugger, get_doubt_solver, get_feedback_collector, get_progress_tracker, get_resource_recommender 

def create_concept_explanation_task(concept, language, simple = False):
  """Create a concept explanation task with dynamic agent""" 
  try:
    agent = get_concept_explainer(concept, language)
    if simple:
      description = f"""Explain the concept of {concept} in {language} in the simplest possible terms,
            - Use very basic language and avoid technical jargon.
            - Give a real-world analogy.
            - Provide a super simple code example.
            - Keep the explanation short and very easy to understand."""
      expected_output = "Very simple, beginner-friendly explanation with analogy and a basic code example."
    else:
      description = f"""Provide a detailed explanation of {concept} in {language}. 
      Begin with a simple definition, then use analogies and real-world scenarios to make the concept relatable. 
      Include at least two practical code examples, each with step-by-step explanations. 
      Highlight common pitfalls and misconceptions, and conclude with a summary of key takeaways.""",
      expected_output = "Comprehensive explanation with 1-2 practical code examples and a concise summary."
    return Task(
      description = description,
      expected_output=expected_output,
      agent=agent,
      verbose=False
    )
  except Exception as e:
    print(f"Agent creation failed: {str(e)}")
    return None

def create_mcq_question_task(concept, language, num_questions=3, difficulty="intermediate"):
    """Create MCQ generation task with dynamic agent"""
  try:
    agent = get_mcq_question_asker(concept, num_questions, difficulty)
    return Task(
      description=f"""Design {num_questions} {difficulty} level multiple-choice questions focused on {concept} in {language}. 
      Each question should have 4 options with only one correct answer.
      Format as: Q1. [Question] A) [Option1] B) [Option2] C) [Option3] D) [Option4] 
      Answer: [Correct Option] 
      Explanation: [1-2 sentences]""",
      expected_output=f"{num_questions} formatted MCQs with answers and explanations",
      agent=agent,
      verbose=False
    )
  except Exception as e:
    print(f"Agent creation failed: {str(e)}")
    return None

def create_coding_question_task(concept, language, difficulty="intermediate"):
    """Create coding problem generation task with dynamic agent"""
  try:
    agent = get_coding_question_asker(concept, difficulty)
    return Task(
      description=f"""Design a {difficulty} level coding problem focused on {concept} in {language}. 
      Clearly state the problem requirements and constraints. 
      Provide sample input and output, and describe the expected approach or logic without revealing the solution. 
      Ensure the problem reinforces the concept explained earlier.""",
      expected_output="A coding challenge with clear requirements, constraints, and sample input/output.",
      agent=agent,
      verbose=False
    )
  except Exception as e:
    print(f"Agent creation failed: {str(e)}")
    return None

def create_solution_evaluation_task(concept, problem, code, language):
    """Create solution evaluation task with dynamic agent"""
  try:
    agent = get_answer_checker(concept, problem, code)
    return Task(
      description=f"""Thoroughly review the student's submitted solution to the {concept} coding problem. 
      Problem: {problem}
      Student's Code: {code}
      Language: {language}
      
      Check for logical correctness, code efficiency, and adherence to the problem requirements. 
      Provide a pass/fail verdict, and include a brief analysis explaining the reasoning behind your assessment.""",
      expected_output="Pass/Fail verdict with detailed logical correctness analysis and reasoning.",
      agent=agent,
      verbose=False
    )
  except Exception as e:
    print(f"Agent creation failed: {str(e)}")
    return None

def create_code_debugging_task(concept, problem, code, language):
    """Create code debugging task with dynamic agent"""
  try:
    agent = get_debugger(concept, problem, code)
    return Task(
      description=f"""Analyze the student's code for the {concept} problem in {language}. 
      Problem: {problem}
      Code to Debug: {code}
      
      Identify all errors or suboptimal practices, specifying the exact line numbers where issues occur. 
      For each error, explain why it is incorrect and provide the corrected code with explanations. 
      If the code is correct, confirm and briefly explain why.""",
      expected_output="Line-by-line error analysis with corrected code and explanations.",
      agent=agent,
      verbose=False
    )
  except Exception as e:
    print(f"Agent creation failed: {str(e)}")
    return None

def create_doubt_resolution_task(concept, question, language):
    """Create doubt resolution task with dynamic agent"""
  try:
    agent = get_doubt_solver(concept, question)
    return Task(
      description=f"""Respond to the student's follow-up question about {concept} in {language}. 
      Student Question: {question}
      
      Give clear, concise answers, using additional examples or analogies if needed. 
      Address any misunderstandings, and encourage further questions to ensure full comprehension.""",
      expected_output="Clear answers with additional examples or analogies as needed.",
      agent=agent,
      verbose=False
    )
  except Exception as e:
    print(f"Agent creation failed: {str(e)}")
    return None

def create_feedback_collection_task(concept, code, language):
    """Create feedback collection task with dynamic agent"""
  try:
    agent = get_feedback_collector(concept, code)
    return Task(
      description=f"""Provide constructive feedback on the student's {concept} solution in {language}.
      Student's Code: {code}
      
      Analyze the code for:
      1. Correctness (Pass/Fail with test results)
      2. Efficiency analysis
      3. Code quality issues  
      4. 1-2 improvement suggestions
      
      Organize the feedback in a structured format.""",
      expected_output="Structured feedback report with ratings and detailed comments.",
      agent=agent,
      verbose=False
    )
  except Exception as e:
    print(f"Agent creation failed: {str(e)}")
    return None

def create_progress_tracking_task(concept, history, performance):
    """Create progress tracking task with dynamic agent"""
  try:
    agent = get_progress_tracker(concept, history, performance)
    return Task(
      description=f"""Update the student's progress metrics for {concept} based on their recent submissions and interactions. 
      Learning History: {history}
      Recent Performance: {performance}
      
      Analyze performance trends, highlight strengths and areas needing improvement, and suggest whether to increase difficulty or review foundational topics. 
      Present the results in a dashboard-style summary.""",
      expected_output="Updated progress dashboard with personalized difficulty recommendations.",
      agent=agent,
      verbose=False
    )
  except Exception as e:
    print(f"Agent creation failed: {str(e)}")
    return None

def create_resource_recommendation_task(concept, language, needs="general learning"):
    """Create resource recommendation task with dynamic agent"""
  try:
    agent = get_resource_recommender(concept, needs)
    return Task(
      description=f"""Curate a list of 3-5 high-quality learning resources for {concept} in {language}. 
      Learning Needs: {needs}
      
      Include a mix of articles, videos, and official documentation. 
      For each resource, provide a one-sentence summary explaining its relevance and value for deeper learning.""",
      expected_output="Curated list of 3-5 resources, each with a brief summary of its value.",
      agent=agent,
      verbose=False
    )
  except Exception as e:
    print(f"Agent creation failed: {str(e)}")
    return None

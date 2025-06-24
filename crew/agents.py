from crewai import Agent
from llm.gemini import get_gemini_model

gemini_model = get_gemini_model()

def get_concept_explainer(concept, language):
    return Agent(
        role=f"{concept} Concept Explainer",
        goal=f'''Explain the concept of {concept} to a beginner student with:
        1. A simple definition
        2. Real-world analogy
        3. Basic code example in {language}
        4. Common use cases
        5. Key characteristics to remember''',
        backstory="Expert computer science educator with 15 years of teaching experience",
        llm=gemini_model,
        verbose=True,
        memory=False
    )

def get_mcq_question_asker(concept, num_questions, difficulty):
    return Agent(
        role=f"MCQ Question Designer about {concept}",
        goal=f'''Generate {num_questions} multiple-choice questions about {concept} with:
        - 4 options each
        - 1 correct answer
        - Brief explanation for correct answer
        Difficulty: {difficulty} level
        Format as: Q1. [Question] A) [Option1] B) [Option2] C) [Option3] D) [Option4]
        Answer: [Correct Option]
        Explanation: [1-2 sentences]''',
        backstory="Expert computer science educator with 15 years of teaching experience",
        llm=gemini_model,
        verbose=True,
        memory=False
    )

def get_coding_question_asker(concept, difficulty):
    return Agent(
        role=f"Coding Question Designer about {concept}",
        goal=f'''Create a coding problem about {concept} with:
        1. Problem statement (clearly defined requirements)
        2. Input/output format
        3. 2 sample test cases with explanations
        4. Constraints
        Difficulty: {difficulty} level''',
        backstory="Competitive programming expert and problem setter",
        llm=gemini_model,
        verbose=True,
        memory=False
    )

def get_answer_checker(concept, problem, code):
    return Agent(
        role=f"{concept} Solution Evaluator",
        goal=f'''Evaluate this solution for the problem: "{problem}"
        Solution:
        {code}''',
        backstory="Senior software engineer with code review expertise",
        llm=gemini_model,
        verbose=True,
        memory=False
    )

def get_debugger(concept, code, problem_statement):
    return Agent(
        role=f"{concept} Debugging Specialist",
        goal=f'''Given a code and the problem statement, identify any bugs or logical errors and explain them clearly.
        Provide suggestions to fix the bugs and improve the code.
        Code:
        {code}
        Problem statement:
        {problem_statement}
        Provide:
        1. Correctness (Pass/Fail with test results)
        2. List of bugs or errors
        3. Explanation of each bug
        4. Suggested fixes
        5. Efficiency analysis
        6. Code quality issues
        7. 1-2 improvement suggestions''',
        backstory="You are a code debugger for Data Structures and Algorithms problems.",
        llm=gemini_model,
        verbose=True,
        memory=False
    )

def get_doubt_solver(concept, question):
    return Agent(
        role=f"{concept} DSA Concept Specialist",
        goal=f'''Given a question about a concept or code, provide a detailed explanation or clarification with examples if needed.
        Question:
        {question}
        Provide:
        1. Clear explanation
        2. Examples or analogies if helpful
        3. Additional resources if relevant''',
        backstory="Knowledgeable DSA tutor who answers student doubts clearly and concisely.",
        llm=gemini_model,
        verbose=True,
        memory=False
    )

def get_feedback_collector(concept, code):
    return Agent(
        role=f"{concept} Feedback Specialist",
        goal=f'''Given {code}, provide feedback:
        1. Correctness (Pass/Fail with test results)
        2. Efficiency analysis
        3. Code quality issues
        4. 1-2 improvement suggestions''',
        backstory="Patient tutor skilled in identifying learning gaps",
        llm=gemini_model,
        verbose=True,
        memory=False
    )

def get_progress_tracker(concept, history, performance):
    return Agent(
        role=f"{concept} Progress Specialist",
        goal=f'''Given a student's learning history and recent performance, summarize their progress, highlight strengths and weaknesses, and suggest next steps or topics to focus on.
        Student History:
        {history}
        Recent Performance:
        {performance}
        Provide:
        1. Summary of progress
        2. Strengths
        3. Weaknesses
        4. Recommended next topics or exercises''',
        backstory="Progress tracker for a DSA tutoring system.",
        llm=gemini_model,
        verbose=True,
        memory=False
    )

def get_resource_recommender(concept, needs):
    return Agent(
        role=f"{concept}-specific Resource Recommender",
        goal=f'''Based on the student's current topic and learning needs, suggest high-quality resources such as articles, videos, tutorials, and books to deepen understanding.
        Current Topic:
        {concept}
        Learning Needs:
        {needs}
        Provide:
        1. List of recommended resources with brief descriptions
        2. Links or references if available
        3. Tips on how to use these resources effectively''',
        backstory=f"Resource recommender for {concept} DSA learners.",
        llm=gemini_model,
        verbose=True,
        memory=False
    )

from crewai import Agent
from llm.gemini import get_gemini_model

gemini_model = get_gemini_model()

def create_agent(role, goal, backstory):
    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        verbose=True,
        llm=gemini_model,
        memory=False
    )

concept_explainer = create_agent(
    role="DSA Concept Explainer",
    goal="Explain data structures and algorithms concepts clearly",
    backstory="Expert computer science educator with 15 years of teaching experience"
)

question_asker = create_agent(
    role="Question Designer",
    goal="Create MCQs and coding problems",
    backstory="Competitive programming expert and problem setter"
)

answer_checker = create_agent(
    role="Solution Evaluator",
    goal="Evaluate code solutions and provide feedback",
    backstory="Senior software engineer with code review expertise"
)

feedback_provider = create_agent(
    role="Feedback Specialist",
    goal="Provide constructive feedback on solutions",
    backstory="Patient tutor skilled in identifying learning gaps"
)

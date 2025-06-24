from crewai import Task

from agents import concept_explainer, mcq_question_asker, coding_question_asker, answer_checker, debugger, doubt_solver, feedback_provider, progress_tracker, resource_recommender

concept_explanation = Task(
    description=(
        "Provide a detailed explanation of the {concept} in {language}. "
        "Begin with a simple definition, then use analogies and real-world scenarios to make the concept relatable. "
        "Include at least two practical code examples, each with step-by-step explanations. "
        "Highlight common pitfalls and misconceptions, and conclude with a summary of key takeaways."
    ),
    expected_output="Comprehensive explanation with 1-2 practical code examples and a concise summary.",
    agent=concept_explainer, 
    verbose=False
)

mcq_question_generation = Task(
    description=(
        "Design a {difficulty} level multiple-choice question focused on the {concept} in {language}. "
        "Clearly state the problem requirements and constraints. "
        "Ensure the problem reinforces the concept explained earlier."
    ),
    expected_output="A question with four options a, b, c and d out of which only one is correct.",
    agent=problem_generator,
    context=[concept_explanation],
    verbose=False
)

coding_question_generation = Task(
    description=(
        "Design a {difficulty} level coding problem focused on the {concept} in {language}. "
        "Clearly state the problem requirements and constraints. "
        "Provide sample input and output, and describe the expected approach or logic without revealing the solution. "
        "Ensure the problem reinforces the concept explained earlier."
    ),
    expected_output="A coding challenge with clear requirements, constraints, and sample input/output.",
    agent=problem_generator,
    context=[concept_explanation],
    verbose=False
)

solution_evaluation = Task(
    description=(
        "Thoroughly review the student's submitted solution to the generated coding problem. "
        "Check for logical correctness, code efficiency, and adherence to the problem requirements. "
        "Provide a pass/fail verdict, and include a brief analysis explaining the reasoning behind your assessment."
    ),
    expected_output="Pass/Fail verdict with detailed logical correctness analysis and reasoning.",
    agent=evaluator,
    context=[problem_generation],
    verbose=False
)

code_debugging = Task(
    description=(
        "Analyze the student's code for the {concept} problem in {language} language. "
        "Identify all errors or suboptimal practices, specifying the exact line numbers where issues occur. "
        "For each error, explain why it is incorrect and provide the corrected code with explanations. "
        "If the code is correct, confirm and briefly explain why."
    ),
    expected_output="Line-by-line error analysis with corrected code and explanations.",
    agent=debugger,
    context=[solution_evaluation],
    verbose=False
)

doubt_resolution = Task(
    description=(
        "Respond to the student's follow-up questions about {concept}. "
        "Give clear, concise answers, using additional examples or analogies if needed. "
        "Address any misunderstandings, and encourage further questions to ensure full comprehension."
    ),
    expected_output="Clear answers with additional examples or analogies as needed.",
    agent=doubt_solver,
    context=[concept_explanation],
    verbose=False
)

feedback_collection = Task(
    description=(
        "Prompt the student to provide feedback on the learning experience so far. "
        "Ask for specific ratings on clarity, engagement, and usefulness, as well as open-ended comments for improvement. "
        "Organize the feedback into a structured report."
    ),
    expected_output="Structured feedback report with ratings and detailed comments.",
    agent=feedback_collector,
    context="",
    verbose=False
)

progress_tracking = Task(
    description=(
        "Update the student's progress metrics for {concept} based on their recent submissions and interactions. "
        "Analyze performance trends, highlight strengths and areas needing improvement, and suggest whether to increase difficulty or review foundational topics. "
        "Present the results in a dashboard-style summary."
    ),
    expected_output="Updated progress dashboard with personalized difficulty recommendations.",
    agent=progress_tracker,
    context=[solution_evaluation, code_debugging],
    verbose=False
)

resource_recommendation = Task(
    description=(
        "Curate a list of 3-5 high-quality learning resources for {concept} in {language}. "
        "Include a mix of articles, videos, and official documentation. "
        "For each resource, provide a one-sentence summary explaining its relevance and value for deeper learning."
    ),
    expected_output="Curated list of 3-5 resources, each with a brief summary of its value.",
    agent=resource_recommender,
    context=[concept_explanation],
    verbose=False
)

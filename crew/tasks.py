from crewai import Task
from agents import (
    concept_explainer,
    problem_generator,
    evaluator,
    debugger,
    doubt_solver,
    feedback_collector,
    progress_tracker,
    resource_recommender
)

# 1. Concept Explanation Task
concept_explanation = Task(
    description="Explain {concept} in {language} with clear examples and analogies",
    expected_output="Comprehensive explanation with 1-2 practical code examples",
    agent=concept_explainer,
    context="",
    verbose=False
)

# 2. Problem Generation Task
problem_generation = Task(
    description="Create a {difficulty} coding problem about {concept} in {language}",
    expected_output="A coding challenge with requirements and sample input/output",
    agent=problem_generator,
    context=[concept_explanation],
    verbose=False
)

# 3. Solution Evaluation Task
solution_evaluation = Task(
    description="Evaluate student's solution to the coding problem",
    expected_output="Pass/Fail verdict with logical correctness analysis",
    agent=evaluator,
    context=[problem_generation],
    verbose=False
)

# 4. Debugging Task
code_debugging = Task(
    description="Identify and explain errors in student's code solution",
    expected_output="Line-by-line error analysis with corrected code",
    agent=debugger,
    context=[solution_evaluation],
    verbose=False
)

# 5. Doubt Resolution Task
doubt_resolution = Task(
    description="Address student's follow-up questions about {concept}",
    expected_output="Clear answers with additional examples if needed",
    agent=doubt_solver,
    context=[concept_explanation],
    verbose=False
)

# 6. Feedback Collection Task
feedback_collection = Task(
    description="Collect student feedback on the learning experience",
    expected_output="Structured feedback report with ratings and comments",
    agent=feedback_collector,
    context="",
    verbose=False
)

# 7. Progress Tracking Task
progress_tracking = Task(
    description="Update student's progress metrics for {concept}",
    expected_output="Updated progress dashboard with difficulty recommendations",
    agent=progress_tracker,
    context=[solution_evaluation, code_debugging],
    verbose=False
)

# 8. Resource Recommendation Task
resource_recommendation = Task(
    description="Suggest learning resources for {concept} in {language}",
    expected_output="Curated list of 3-5 high-quality resources",
    agent=resource_recommender,
    context=[concept_explanation],
    verbose=False
)

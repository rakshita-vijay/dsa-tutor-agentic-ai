from crewai import Crew
from llm.gemini import my_llm

from agents import concept_explainer, mcq_question_asker, coding_question_asker, answer_checker, debugger, doubt_solver, feedback_provider, progress_tracker, resource_recommender 
 
from tasks import concept_explanation, problem_generation, solution_evaluation, code_debugging, doubt_resolution, feedback_collection, progress_tracking, resource_recommendation

crewww = Crew(
  agents = [concept_explainer, problem_generator, evaluator, debugger, doubt_solver, feedback_collector, progress_tracker, resource_recommender],
  tasks = [concept_explanation, problem_generation, solution_evaluation, code_debugging, doubt_resolution, feedback_collection, progress_tracking, resource_recommendation],
  process = "sequential",
  verbose = False,
  memory = False,
  share_crew = True,
  planning = False,
  chat_llm = my_llm
)

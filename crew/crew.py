from crewai import Crew
from llm.gemini import my_llm

from crew.agents import (get_concept_explainer, get_mcq_question_asker,  get_coding_question_asker, get_answer_checker, get_debugger, get_doubt_solver,  get_feedback_collector,  get_progress_tracker,  get_resource_recommender)

from crew.tasks import (create_concept_explanation_task, create_mcq_question_task, create_coding_question_task, create_solution_evaluation_task, create_code_debugging_task, create_doubt_resolution_task, create_feedback_collection_task, create_progress_tracking_task, create_resource_recommendation_task) 

crewww = Crew(
  agents = [get_concept_explainer, get_mcq_question_asker,  get_coding_question_asker, get_answer_checker, get_debugger, get_doubt_solver,  get_feedback_collector,  get_progress_tracker,  get_resource_recommender],
 
  tasks = [create_concept_explanation_task, create_mcq_question_task, create_coding_question_task, create_solution_evaluation_task, create_code_debugging_task, create_doubt_resolution_task, create_feedback_collection_task, create_progress_tracking_task, create_resource_recommendation_task],
 
  process = "sequential",
  verbose = False,
  memory = False,
  share_crew = True,
  planning = False,
  chat_llm = my_llm
)

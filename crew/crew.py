from crewai import Crew, Process
from llm.gemini import get_gemini_model

class DSACrew:
  def __init__(self):
    self.llm = get_gemini_model

  def run_task(self, task_creator, *args):
    """Dynamically creates and executes a task with its agent"""
    try:
      task = task_creator(*args)
      if not task:
        return "Task creation failed"
          
      crew = Crew(
        agents=[task.agent],
        tasks=[task],
        process=Process.sequential,
        verbose=2,
        memory=False
      )
      return crew.kickoff()
    except Exception as e:
      return f"Error: {str(e)}"

# Example usage in app.py:
# dsa_crew = DSACrew()
# explanation = dsa_crew.run_task(create_concept_explanation_task, concept, language)


# from crewai import Crew
# from llm.gemini import get_gemini_model

# from crew.agents import (get_concept_explainer, get_mcq_question_asker,  get_coding_question_asker, get_answer_checker, get_debugger, get_doubt_solver,  get_feedback_collector,  get_progress_tracker,  get_resource_recommender)

# from crew.tasks import (create_concept_explanation_task, create_mcq_question_task, create_coding_question_task, create_solution_evaluation_task, create_code_debugging_task, create_doubt_resolution_task, create_feedback_collection_task, create_progress_tracking_task, create_resource_recommendation_task) 

# crewww = Crew(
#   agents = [get_concept_explainer, get_mcq_question_asker,  get_coding_question_asker, get_answer_checker, get_debugger, get_doubt_solver,  get_feedback_collector,  get_progress_tracker,  get_resource_recommender],
 
#   tasks = [create_concept_explanation_task, create_mcq_question_task, create_coding_question_task, create_solution_evaluation_task, create_code_debugging_task, create_doubt_resolution_task, create_feedback_collection_task, create_progress_tracking_task, create_resource_recommendation_task],
 
#   process = "sequential",
#   verbose = False,
#   memory = False,
#   share_crew = True,
#   planning = False,
#   chat_llm = get_gemini_model
# )


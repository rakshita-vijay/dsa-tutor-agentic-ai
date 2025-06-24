from crewai import Crew
from crew.agents import (concept_explainer, mcq_question_asker, coding_question_asker, answer_checker, feedback_provider)
from crew.tasks import (concept_explanation, problem_generation, solution_evaluation, code_debugging, doubt_resolution, feedback_collection, progree_tracking, resource_recommendation)
from crew.crew import crewww

import streamlit as st

def run_concept_explanation():
    try:
        concept_crew = Crew(
            agents=[concept_explainer],
            tasks=[concept_explanation],
            verbose=False
        )
        inputs = {
            'concept': st.session_state.selected_topic,
            'language': st.session_state.selected_language
        }
        result = concept_crew.kickoff(inputs=inputs)
        return result.raw if hasattr(result, 'raw') else str(result)
    except Exception as e:
        st.error(f"Error in concept explanation: {str(e)}")
        return None    

def run_mcq_generation():
    try:
        mcq_crew = Crew(
            agents = [mcq_question_asker],
            tasks = [


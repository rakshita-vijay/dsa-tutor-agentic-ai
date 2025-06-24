from crewai import Crew
from crew.agents import (concept_explainer, problem_generator, evaluator, debugger, doubt_solver, feedback_collector, progress_tracker, resource_recommender)
from crew.tasks import (concept_explanation, problem_generation, solution_evaluation, code_debugging, doubt_resolution, feedback_collection, progree_tracking, resource_recommendation)
from crew.crew import crewww

import streamlit as st

def run_concept_explanation():
    explanation = concept_explanation(
        concept=st.session_state.selected_topic,
        language=st.session_state.selected_language
    )
    return explanation

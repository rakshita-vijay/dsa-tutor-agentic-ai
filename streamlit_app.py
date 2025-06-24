import sys
import importlib

importlib.import_module("pysqlite3")
sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

import os
os.environ["CHROMA_DISABLE_SQLITE_VERSION_CHECK"] = "1"


import streamlit as st
from crew.agents import (
    concept_explainer, problem_generator, evaluator, debugger,
    doubt_solver, feedback_collector, progress_tracker, resource_recommender
)
from crew.crew import crewww

# --- Wrapper functions to call agents ---
def concept_explainer_call(language, topic, simpler=False):
    prompt = f"Explain the concept of {topic} in {language}."
    if simpler:
        prompt += " Use even simpler words, analogies, and step-by-step breakdowns."
    return concept_explainer.run(prompt)

def problem_generator_call(language, topic):
    prompt = f"Generate a relevant coding exercise and conceptual question on {topic} in {language}."
    return problem_generator.run(prompt)

# --- Session State Initialization ---
if 'step' not in st.session_state:
    st.session_state.step = 'language_selection'
if 'language' not in st.session_state:
    st.session_state.language = None
if 'topic' not in st.session_state:
    st.session_state.topic = None
if 'explanation' not in st.session_state:
    st.session_state.explanation = ''
if 'understood' not in st.session_state:
    st.session_state.understood = None
if 'question' not in st.session_state:
    st.session_state.question = ''
if 'questions_asked' not in st.session_state:
    st.session_state.questions_asked = 0

st.title("DSA Tutor Bot")
st.caption("Interactive learning for Data Structures & Algorithms")

if st.session_state.step == 'language_selection':
    language = st.selectbox("Choose your programming language:", ["Python", "Java", "C", "C++"])
    if st.button("Next"):
        st.session_state.language = language
        st.session_state.step = 'topic_selection'
        st.experimental_rerun()

elif st.session_state.step == 'topic_selection':
    topic = st.selectbox("Choose a DSA topic:", [
        "Array", "String", "Linked List", "Stack", "Queue", 
        "Tree", "Graph", "Sorting", "Searching", "Dynamic Programming"
    ])
    if st.button("Next"):
        st.session_state.topic = topic
        st.session_state.explanation = concept_explainer_call(
            st.session_state.language, st.session_state.topic)
        st.session_state.step = 'explanation'
        st.experimental_rerun()

elif st.session_state.step == 'explanation':
    st.subheader(f"Explanation of {st.session_state.topic} in {st.session_state.language}")
    st.write(st.session_state.explanation)
    understood = st.radio("Did you understand the explanation?", ["Yes", "No"])
    if st.button("Submit"):
        st.session_state.understood = (understood == "Yes")
        if not st.session_state.understood:
            st.session_state.explanation = concept_explainer_call(
                st.session_state.language, st.session_state.topic, simpler=True)
            st.experimental_rerun()
        else:
            st.session_state.question = problem_generator_call(
                st.session_state.language, st.session_state.topic)
            st.session_state.questions_asked = 1
            st.session_state.step = 'question'
            st.experimental_rerun()

elif st.session_state.step == 'question':
    st.subheader(f"Practice Question {st.session_state.questions_asked} on {st.session_state.topic} in {st.session_state.language}")
    st.write(st.session_state.question)
    more = st.radio("Do you want another question?", ["Yes", "No"])
    if st.button("Submit"):
        if more == "Yes":
            st.session_state.question = problem_generator_call(
                st.session_state.language, st.session_state.topic)
            st.session_state.questions_asked += 1
            st.experimental_rerun()
        else:
            st.success("Thank you for practicing! You can restart or choose a new topic.")
            if st.button("Restart"):
                for key in ['step', 'language', 'topic', 'explanation', 'understood', 'question']:
                    st.session_state[key] = None if key != 'step' else 'language_selection'
                st.session_state.questions_asked = 0
                st.experimental_rerun()

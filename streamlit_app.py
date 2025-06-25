import streamlit as st
from crew.crew import DSACrew
from crew.tasks import (
    create_concept_explanation_task,
    create_mcq_question_task,
    create_solution_evaluation_task
)

# --- Constants ---
LANGUAGES = ["Java", "Python", "C", "C++"]
TOPICS = ["Array", "Strings", "Linked List", "Stack", "Queue", "Tree", "Graph", "Sorting", "Searching"]

# --- Session State Initialization ---
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.language = None
    st.session_state.topic = None
    st.session_state.simple = False
    st.session_state.explanation = ""
    st.session_state.question = ""
    st.session_state.correct_answer = ""
    st.session_state.feedback = ""
    st.session_state.user_answer = ""
    st.session_state.ask_more = True

dsa_crew = DSACrew()

# --- Step 1: Language Selection ---
if st.session_state.step == 1:
    st.header("Select Programming Language")
    st.session_state.language = st.selectbox("Choose language:", LANGUAGES)
    if st.button("Next"):
        st.session_state.step = 2

# --- Step 2: Topic Selection ---
elif st.session_state.step == 2:
    st.header("Select DSA Topic")
    st.session_state.topic = st.selectbox("Choose topic:", TOPICS)
    if st.button("Next"):
        st.session_state.step = 3
        st.session_state.simple = False  # Start with normal explanation

# --- Step 3: Concept Explanation ---
elif st.session_state.step == 3:
    st.header(f"Explaining: {st.session_state.topic} in {st.session_state.language}")
    if not st.session_state.explanation:
        # Get explanation (simple or normal)
        task = create_concept_explanation_task(
            st.session_state.topic, st.session_state.language, st.session_state.simple
        )
        st.session_state.explanation = dsa_crew.run_task(
            create_concept_explanation_task,
            st.session_state.topic, st.session_state.language, st.session_state.simple
        )
    st.markdown(st.session_state.explanation)
    understood = st.radio("Did you understand?", ["Understood", "Not Understood"])
    if st.button("Continue"):
        if understood == "Understood":
            st.session_state.step = 4
            st.session_state.explanation = ""  # Reset for next time
        else:
            st.session_state.simple = True  # Request simpler explanation
            st.session_state.explanation = ""  # Force re-explanation

# --- Step 4: Ask a Question ---
elif st.session_state.step == 4:
    st.header(f"Question on {st.session_state.topic}")
    if not st.session_state.question:
        # Generate MCQ question
        st.session_state.question = dsa_crew.run_task(
            create_mcq_question_task,
            st.session_state.topic, st.session_state.language, 1, "easy"
        )
    st.markdown(st.session_state.question)
    st.session_state.user_answer = st.text_input("Your Answer (e.g., A, B, C, D):")
    if st.button("Submit Answer"):
        st.session_state.step = 5

# --- Step 5: Check Answer & Feedback ---
elif st.session_state.step == 5:
    st.header("Checking Your Answer")
    # Evaluate answer (assuming MCQ format)
    feedback = dsa_crew.run_task(
        create_solution_evaluation_task,
        st.session_state.topic, st.session_state.question, st.session_state.user_answer, st.session_state.language
    )
    st.markdown(feedback)
    more = st.radio("Do you want another question?", ["Yes", "No"])
    if st.button("Continue"):
        if more == "Yes":
            st.session_state.step = 4
            st.session_state.question = ""
            st.session_state.user_answer = ""
        else:
            st.session_state.step = 6

# --- Step 6: End or Restart ---
elif st.session_state.step == 6:
    st.header("Session Complete")
    if st.button("Restart"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()


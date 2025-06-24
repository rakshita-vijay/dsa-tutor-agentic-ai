import streamlit as st

from crewai import Crew
from crew.tasks import create_concept_explanation_task, create_mcq_question_task, create_coding_question_task, create_solution_evaluation_task, create_code_debugging_task, create_doubt_resolution_task, create_feedback_collection_task, create_progress_tracking_task,create_resource_recommendation_task

# --- Step 1: Language selection ---
if "language" not in st.session_state:
    st.session_state.language = None
if "topic" not in st.session_state:
    st.session_state.topic = None
if "explained" not in st.session_state:
    st.session_state.explained = False
if "explanation" not in st.session_state:
    st.session_state.explanation = ""
if "understood" not in st.session_state:
    st.session_state.understood = None
if "question_count" not in st.session_state:
    st.session_state.question_count = 0
if "last_question" not in st.session_state:
    st.session_state.last_question = ""
if "more_questions" not in st.session_state:
    st.session_state.more_questions = True

# 1. Language selection
if not st.session_state.language:
    st.session_state.language = st.selectbox("Choose programming language:", ["Python", "Java", "C", "C++"])
    st.stop()

# 2. Topic selection
if not st.session_state.topic:
    st.session_state.topic = st.selectbox(
        "Choose a DSA topic:",
        ["Array", "String", "Linked List", "Stack", "Queue", "Tree", "Graph", "Hash Table"]
    )
    st.stop()

# 3. Concept explanation
if not st.session_state.explained or st.session_state.understood is False:
    # Decide if we want a simple explanation (if user did not understand)
    simple = st.session_state.explained and st.session_state.understood is False

    if st.button(
        "Explain the topic" if not st.session_state.explained else "Explain again (simpler)"
    ):
        task = create_concept_explanation_task(
            st.session_state.topic,
            st.session_state.language,
            simple=simple
        )
        st.session_state.explanation = (
            task.execute() if hasattr(task, "execute") else task.run()
        )
        st.session_state.explained = True
        st.session_state.understood = None
        st.experimental_rerun()

    if st.session_state.explanation:
        st.markdown("### Explanation")
        st.write(st.session_state.explanation)
        st.session_state.understood = (
            st.radio(
                "Did you understand the explanation?",
                ("Yes", "No"),
                index=0
                if st.session_state.understood is None
                else (0 if st.session_state.understood else 1),
            )
            == "Yes"
        )
        if st.button("Continue"):
            st.experimental_rerun()
    st.stop()


# 4. Question loop
if st.session_state.understood and st.session_state.more_questions:
    if st.button("Get a question", key=f"q{st.session_state.question_count}"):
        st.session_state.question_count += 1
        task = create_mcq_question_task(
            st.session_state.topic,
            st.session_state.language,
            num_questions=1,
            difficulty="easy"
        )
        st.session_state.last_question = task.execute() if hasattr(task, "execute") else task.run()
        st.experimental_rerun()
    if st.session_state.last_question:
        st.markdown("### Practice Question")
        st.write(st.session_state.last_question)
        st.session_state.more_questions = st.radio(
            "Would you like another question?",
            ("Yes", "No"),
            index=0
        ) == "Yes"
        if st.button("Next"):
            if st.session_state.more_questions:
                st.session_state.last_question = ""
                st.experimental_rerun()
            else:
                st.success("Great job! You can restart or choose a new topic/language from the sidebar.")
                st.stop()


import streamlit as st
from crew import DSACrew
from tasks import create_concept_explanation_task, create_mcq_question_task, create_solution_evaluation_task

# Initialize session state
if "step" not in st.session_state:
    st.session_state.update({
        "step": 0,
        "language": None,
        "topic": None,
        "concept_explained": False,
        "understood": False,
        "question": "",
        "user_answer": "",
        "feedback": "",
        "ask_more": True
    })

dsa_crew = DSACrew()

# Step 0: Language Selection
if st.session_state.step == 0:
    st.header("🚀 Welcome to DSA Tutor!")
    st.session_state.language = st.selectbox(
        "Select programming language:",
        ["Python", "Java", "C", "C++"]
    )
    if st.button("Next"):
        st.session_state.step = 1

# Step 1: Topic Selection
elif st.session_state.step == 1:
    st.header(f"Language: {st.session_state.language}")
    st.session_state.topic = st.selectbox(
        "Choose DSA topic:",
        ["Arrays", "Strings", "Linked Lists", "Stacks", "Queues", "Trees", "Graphs"]
    )
    if st.button("Start Learning"):
        st.session_state.step = 2
        st.session_state.concept_explained = False

# Step 2: Concept Explanation
elif st.session_state.step == 2 and not st.session_state.concept_explained:
    st.header(f"📚 {st.session_state.topic} in {st.session_state.language}")
    with st.spinner("Generating explanation..."):
        explanation = dsa_crew.run_task(
            create_concept_explanation_task,
            st.session_state.topic,
            st.session_state.language,
            simple=st.session_state.understood  # Simplify if not understood before
        )
    st.markdown(explanation)
    st.session_state.concept_explained = True
    
    if st.button("Understood! Give me a question"):
        st.session_state.step = 3
    elif st.button("Explain again in simpler terms"):
        st.session_state.understood = True
        st.session_state.concept_explained = False
        st.experimental_rerun()

# Step 3: Ask Question
elif st.session_state.step == 3:
    if not st.session_state.question:
        with st.spinner("Generating question..."):
            st.session_state.question = dsa_crew.run_task(
                create_mcq_question_task,
                st.session_state.topic,
                st.session_state.language,
                1,  # 1 question
                "easy"
            )
    
    st.header(f"❓ Question on {st.session_state.topic}")
    st.markdown(st.session_state.question)
    st.session_state.user_answer = st.text_input("Your answer (A/B/C/D):", max_chars=1).upper()
    
    if st.button("Submit Answer"):
        st.session_state.step = 4

# Step 4: Check Answer
elif st.session_state.step == 4:
    with st.spinner("Checking your answer..."):
        feedback = dsa_crew.run_task(
            create_solution_evaluation_task,
            st.session_state.topic,
            st.session_state.question,
            st.session_state.user_answer,
            st.session_state.language
        )
        st.session_state.feedback = feedback
    
    st.header("📝 Feedback")
    st.markdown(feedback)
    
    if st.button("Another question"):
        st.session_state.question = ""
        st.session_state.user_answer = ""
        st.session_state.feedback = ""
        st.session_state.step = 3
        st.experimental_rerun()
    elif st.button("Start over with new topic"):
        st.session_state.step = 1
        st.session_state.concept_explained = False
        st.session_state.understood = False
        st.experimental_rerun()

# Add restart option
if st.session_state.step > 0:
    if st.button("Restart Session"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()


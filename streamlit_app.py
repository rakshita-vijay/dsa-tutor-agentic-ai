import streamlit as st
from crew.agents import concept_explainer, problem_generator

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

# --- Agent Functions ---
def concept_explainer_call(language, topic, simpler=False):
    prompt = f"Explain the concept of {topic} in {language}."
    if simpler:
        prompt += " Use even simpler words and more analogies."
    return concept_explainer.run(prompt)

def problem_generator_call(language, topic):
    prompt = f"Generate a coding exercise on {topic} in {language}."
    return problem_generator.run(prompt)

# --- Streamlit App Logic ---
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
        "Array", "String", "Linked List", "Stack", "Queue", "Tree", "Graph", "Sorting", "Searching", "Dynamic Programming"
    ])
    if st.button("Next"):
        st.session_state.topic = topic
        # Get initial explanation from agent
        st.session_state.explanation = concept_explainer(st.session_state.language, st.session_state.topic)
        st.session_state.step = 'explanation'
        st.experimental_rerun()

elif st.session_state.step == 'explanation':
    st.subheader(f"Explanation of {st.session_state.topic} in {st.session_state.language}")
    st.write(st.session_state.explanation)
    understood = st.radio("Did you understand the explanation?", ["Yes", "No"])
    if st.button("Submit"):
        st.session_state.understood = (understood == "Yes")
        if not st.session_state.understood:
            # Ask agent for a simpler explanation
            st.session_state.explanation = concept_explainer(
                st.session_state.language, st.session_state.topic, simpler=True)
            st.experimental_rerun()
        else:
            # Move to first question
            st.session_state.question = problem_generator(
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
            st.session_state.question = problem_generator(
                st.session_state.language, st.session_state.topic)
            st.session_state.questions_asked += 1
            st.experimental_rerun()
        else:
            st.success("Thank you for practicing! You can restart or choose a new topic.")
            if st.button("Restart"):
                for key in ['step', 'language', 'topic', 'explanation', 'understood', 'question', 'questions_asked']:
                    st.session_state[key] = None if key != 'step' else 'language_selection'
                st.experimental_rerun()

import streamlit as st

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("DSA Tutor Bot")
st.subheader("Learn Data Structures & Algorithms")

# Sidebar for agent controls
with st.sidebar:
    st.header("Agent Configuration")
    language = st.selectbox("Programming Language", ["Python", "Java", "C++", "C"])
    difficulty = st.select_slider("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
    topic = st.selectbox("DSA Topic", ["Arrays", "Linked Lists", "Stacks", "Queues", "Trees", "Graphs", "Sorting", "Searching", "DP"])

# Main chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# File upload for course materials
uploaded_file = st.file_uploader("Upload DSA materials", type=["pdf", "txt", "md"])
if uploaded_file:
    st.success(f"Processing {uploaded_file.name}...")

# Chat input
if prompt := st.chat_input("Ask about linked lists, sorting algorithms..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Consulting tutor agents..."):
            response = get_agent_response(prompt)  # Connect to your CrewAI agents
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# dsa-tutor-agentic-ai

### **File Structure**
```
dsa-tutor-agentic-ai/
├── .env                      # Store secrets like GEMINI_API_KEY
├── requirements.txt          # List of dependencies
├── README.md                 # Project overview and setup
├── streamlit_app.py          # Main Streamlit UI entry point
├── crew/
│   ├── __init__.py
│   ├── agents.py             # All agent classes/instances defined here
│   ├── tasks.py              # Task definitions and orchestration logic
│   ├── crew.py               # Crew creation and workflow management
│   └── tools.py              # Custom tools for agents (e.g., code runner)
├── llm/
│   ├── __init__.py
│   └── gemini.py             # Gemini API wrapper/setup
├── utils/
│   ├── __init__.py
│   └── prompts.py            # Prompt templates and helpers
├── assets/                   # Images, logos, custom CSS, etc.
└── .streamlit/
    └── config.toml           # Streamlit config (theme, etc.)
```


---


## **Agents Required:**

#### **1. Concept Explainer:**
* This agent is the primary tutor who shall explain core concepts.

* Example:
"An array is a collection of elements that are stored in a contiguous block of memory, and all elements are of the same data type.
Think of it like a row of boxes — each box (called an element) holds a value, and you can access each box using its index number....."


#### **2. Ask Questions and Codes:**
* This agent generates exercises and coding problems after explanations, promoting active learning.

* Example:
"Write a C program to do the following: Declare an array of 10 integers, take input from the user to fill the array and print only the even numbers from the array."


#### **3. Answer Checker:**
* This agent evaluates student submissions, providing immediate feedback on correctness.

* Example:
"That is the correct answer." or "That is not the correct answer."

#### **4. Bug Lister:**
* This agent lists out the lines where the student has made a mistake, and provides the correct solution, line-wise.

* Example:
"Line 5 has a mistake. (mistake detailed) \n That is the correct answer. (details oout the correct answer)"

#### **5. Doubt Solver:**
* This agent addresses student questions, clarifies misunderstandings, and provides additional support.

* Example:
"Great Doubt! The last element of an array is at index size - 1 because array indexing starts from 0, not 1....."


#### **6. Feedback:**
* This agent collects feedback from students on the tutoring process, enabling personalization.


#### **7. Progress Tracker:**
* Monitors student performance over time and adapts content difficulty or suggests review topics.

#### **8. Resource Recommender:**
* Suggests supplementary materials (videos, articles, documentation) for deeper learning.

# dsa-tutor-agentic-ai

### **File Structure**
```
dsa_tutor/
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

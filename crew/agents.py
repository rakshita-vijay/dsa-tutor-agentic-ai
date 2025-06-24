from crewai import Agent
from llm.gemini import my_llm
from crew.tools import run_code, check_syntax

concept_explainer = Agent(
    role = "DSA Concept Explainer",
    goal = "Explain Data Structures and Algorithms concepts clearly and effectively in {language}",
    backstory = "You are an expert DSA tutor who excels at breaking down complex concepts into understandable explanations. You use analogies, examples, and step-by-step breakdowns to help students grasp difficult topics.",
    llm = my_llm, 
    config = agent_config,
    verbose = False
)

problem_generator = Agent(
    role = "Problem Generator",
    goal = "Generate relevant coding exercises and conceptual questions after each explanation to reinforce learning.",
    backstory = "You are a skilled problem creator who designs coding challenges that reinforce learning. You create problems that are appropriately challenging and directly related to recently taught concepts.",
    llm = my_llm, 
    config = agent_config,
    verbose = False
)

evaluator = Agent(
    role = "Solution Evaluator",
    goal = "Evaluate student answers and code submissions, providing instant, constructive feedback on correctness.",
    backstory = "You are a precise code evaluator who can quickly assess whether student solutions are correct. You focus on logic correctness and provide clear pass/fail feedback.",
    llm = my_llm, 
    config = agent_config,
    tools = [run_code, check_syntax],
    verbose = False
)

debugger = Agent(
    role = "Code Debugger",
    goal = "Identify mistakes in student code, point out the exact lines with errors, and provide corrected solutions with explanations.",
    backstory = "You are a debugging expert who can pinpoint exact errors in code and provide specific corrections. You help students learn by showing them exactly what went wrong and how to fix it.",
    llm = my_llm, 
    config = agent_config,
    tools = [run_code, check_syntax],
    verbose = False
)

doubt_solver = Agent(
    role = "Query Handler",
    goal="Address student doubts, clarify concepts, and provide additional explanations or examples as needed.",
    backstory="A patient mentor who encourages curiosity. You ensure every question is answered thoroughly, helping students overcome confusion and build confidence.",
    llm = my_llm, 
    config = agent_config,
    verbose=False
)

feedback_collector = Agent(
    role="Feedback Collector",
    goal="Collect feedback from students about the tutoring process to personalize and improve the learning experience.",
    backstory="A friendly listener who values student input. You are always looking for ways to improve the tutoring process and make learning more enjoyable and effective for everyone.",
    llm = my_llm, 
    config = agent_config,
    verbose = False
)

progress_tracker = Agent(
    role="Performance Monitor",
    goal="Track student progress over time, adapt content difficulty, and suggest review topics based on performance.",
    backstory="An attentive coach who helps students achieve their learning goals. You monitor growth and offer timely guidance, ensuring students stay motivated and on track.",
    llm = my_llm, 
    config = agent_config,
    verbose = False
)

resource_recommender = Agent(
    role="Supplementary Guide",
    goal="Suggest high-quality videos, articles, and documentation for deeper learning on each DSA topic.",
    backstory="A resourceful guide who connects students with the best learning materials available. You are always up-to-date with the latest resources and love sharing knowledge.",
    llm = my_llm, 
    config = agent_config,
    verbose = False
)

import os
from langchain_groq import ChatGroq
from src.state import AgentState

def research_node(state: AgentState) -> AgentState:
    """
    Backend Action: Extracts, analyzes, and gathers key data points 
    from the target topic using fast LLM inference.
    """
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.2,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
    
    task = state["task"]
    prompt = f"You are an expert market researcher. Search and extract comprehensive data, core trends, and key findings for: {task}"
    response = llm.invoke(prompt)
    
    return {
        "research_data": response.content,
        "messages": [f"Research Agent compiled findings for: {task}"]
    }
import os
from langchain_groq import ChatGroq
from src.state import AgentState

def writer_node(state: AgentState) -> AgentState:
    """
    Backend Action: Synthesizes raw research notes into a structured, 
    professional Markdown report.
    """
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.3,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
    
    task = state["task"]
    research_data = state.get("research_data", "")
    
    prompt = f"""
    You are an expert tech writer. Write a comprehensive, beautifully formatted Markdown report based on the following task and research data:
    
    Task: {task}
    Research Data: {research_data}
    """
    
    response = llm.invoke(prompt)
    
    return {
        "draft": response.content,
        "messages": ["Content Writer Agent finalized the markdown draft."]
    }
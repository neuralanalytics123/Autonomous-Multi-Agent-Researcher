from src.state import AgentState

def supervisor_node(state: AgentState) -> AgentState:
    """Routes execution between research and writing."""
    messages = state.get("messages", [])
    if not any("Research" in m for m in messages):
        next_step = "researcher"
    elif not any("Writer" in m for m in messages):
        next_step = "writer"
    else:
        next_step = "FINISH"
        
    return {
        "next_agent": next_step,
        "messages": [f"Supervisor routed next step to: {next_step}"]
    }

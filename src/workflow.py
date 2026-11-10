from langgraph.graph import StateGraph, END
from src.state import AgentState
from src.agents.supervisor import supervisor_node
from src.agents.researcher import research_node
from src.agents.writer import writer_node

def create_workflow():
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("supervisor", supervisor_node)
    workflow.add_node("researcher", research_node)
    workflow.add_node("writer", writer_node)

    # Set entry point
    workflow.set_entry_point("supervisor")

    # Add conditional routing edges
    workflow.add_conditional_edges(
        "supervisor",
        lambda state: state["next_agent"],
        {
            "researcher": "researcher",
            "writer": "writer",
            "FINISH": END
        }
    )

    workflow.add_edge("researcher", "supervisor")
    workflow.add_edge("writer", "supervisor")

    return workflow.compile()

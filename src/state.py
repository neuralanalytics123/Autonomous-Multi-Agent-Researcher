from typing import TypedDict, List, Annotated
import operator

class AgentState(TypedDict):
    task: str
    research_data: str
    draft: str
    feedback: str
    messages: Annotated[List[str], operator.add]
    next_agent: str

from langgraph.graph import StateGraph
from agents import planner_agent, analysis_agent, decision_agent

workflow = StateGraph(dict)

workflow.add_node("planner", planner_agent)
workflow.add_node("analysis", analysis_agent)
workflow.add_node("decision", decision_agent)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "analysis")
workflow.add_edge("analysis", "decision")

workflow.set_finish_point("decision")   # IMPORTANT

graph = workflow.compile()
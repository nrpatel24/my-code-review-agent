# agent_graph/graph.py

from langgraph.graph import StateGraph
from agents.pipeline import pipeline_agent

def create_graph(model="openai", server=None, model_endpoint=None):
    graph = StateGraph(dict)
    graph.add_node(
        "pipeline",
        lambda state: pipeline_agent(
            state,
            model=model,
            server=server,
            stop=None,
            model_endpoint=model_endpoint
        )
    )
    graph.set_entry_point("pipeline")
    graph.set_finish_point("pipeline")
    return graph

def compile_workflow(graph):
    return graph.compile()

# agent_graph/graph.py

from langgraph.graph import StateGraph
from agents.code_reviewer import code_review_agent

def create_graph(model="openai", server=None, model_endpoint=None):
    graph = StateGraph(dict)

    graph.add_node(
        "code_review",
        lambda state: code_review_agent(
            state,
            file_path=state["code_file"],
            model=model,
            server=server,
            stop=None,
            model_endpoint=model_endpoint,
        )
    )

    graph.set_entry_point("code_review")
    graph.set_finish_point("code_review")
    return graph

def compile_workflow(graph):
    return graph.compile()

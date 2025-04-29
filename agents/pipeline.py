# agents/pipeline.py

from agents.splitter import split_file_agent
from agents.code_reviewer import code_review_agent
from agents.aggregator import aggregate_reviews_agent

def pipeline_agent(state, *, model=None, server=None, stop=None, model_endpoint=None):
    # 1) Split the file
    state = split_file_agent(state, file_path=state["code_file"])
    chunks = state.get("chunks", [])

    # 2) Review each chunk sequentially
    reviews = []
    for chunk in chunks:
        out = code_review_agent(
            state={},
            code_chunk=chunk,
            model=model,
            server=server,
            stop=stop,
            model_endpoint=model_endpoint
        )
        raw = out.get("review_comments", "")
        print("DEBUG ▶ raw chunk review:", raw)    # see exactly what LLM returned
        reviews.append(raw)

    state["chunk_reviews"] = reviews

    # 3) Aggregate into one JSON
    state = aggregate_reviews_agent(state)
    return state

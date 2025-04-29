# agents/aggregator.py

import json

def aggregate_reviews_agent(state, **kwargs):
    """
    Merges all JSON strings in state['chunk_reviews'] into one JSON object.
    Writes it to state['review_comments'].
    """
    merged = {"issues": []}
    for chunk_json in state.get("chunk_reviews", []):
        part = json.loads(chunk_json)
        merged["issues"].extend(part.get("issues", []))
    state["review_comments"] = json.dumps(merged, indent=2)
    return state

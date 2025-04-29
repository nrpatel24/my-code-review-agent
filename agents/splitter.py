# agents/splitter.py

def split_file_agent(state, *, file_path, chunk_size=200):
    """
    Splits the Python file at file_path into chunks of ~chunk_size lines.
    Stores a list of code‐string chunks in state['chunks'].
    """
    text = open(file_path, encoding="utf8").read()
    lines = text.splitlines(keepends=True)
    chunks = []
    for i in range(0, len(lines), chunk_size):
        chunks.append("".join(lines[i : i + chunk_size]))
    state["chunks"] = chunks
    return state

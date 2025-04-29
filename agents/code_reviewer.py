# agents/code_reviewer.py

from langchain_core.messages import HumanMessage
from models.openai_models import get_open_ai_json
from prompts.prompts import code_review_prompt_template

def code_review_agent(state, *, file_path=None, code_chunk=None, model=None, server=None, stop=None, model_endpoint=None):
    """
    Reviews either the code_chunk string or the file at file_path.
    Returns {"review_comments": <clean JSON string>}.
    """
    if code_chunk is not None:
        code = code_chunk
    else:
        with open(file_path, encoding="utf8") as f:
            code = f.read()

    llm = get_open_ai_json(model=model)
    prompt = code_review_prompt_template.format(code=code)

    try:
        resp = llm.invoke([HumanMessage(content=prompt)])
        review_text = resp.content
    except AttributeError:
        result = llm([HumanMessage(content=prompt)])
        review_text = result.generations[0][0].message.content

    return {"review_comments": review_text.strip()}
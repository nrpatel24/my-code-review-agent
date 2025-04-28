# agents/code_reviewer.py

from langchain_core.messages import HumanMessage
from models.openai_models import get_open_ai_json
from prompts.prompts import code_review_prompt_template

def code_review_agent(state, *, file_path, model, server, stop, model_endpoint):
    # load the code
    with open(file_path, encoding="utf8") as f:
        code = f.read()

    # prepare LLM
    llm = get_open_ai_json(model=model)

    # build prompt
    prompt = code_review_prompt_template.format(code=code)

    # invoke the model
    try:
        resp = llm.invoke([HumanMessage(content=prompt)])
        review_text = resp.content
    except AttributeError:
        result = llm([HumanMessage(content=prompt)])
        review_text = result.generations[0][0].message.content

    # strip whitespace so JSON starts immediately
    review = review_text.strip()

    # place into state
    state["review_comments"] = review
    return state

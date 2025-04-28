# app/app.py

import argparse
from agents.code_reviewer import code_review_agent

def main():
    parser = argparse.ArgumentParser(description="Run the code‐review agent")
    parser.add_argument(
        "--code-file",
        required=True,
        help="Path to the Python file to review"
    )
    parser.add_argument(
        "--model",
        default="gpt-3.5-turbo-1106",
        help="LLM model (default: gpt-3.5-turbo-1106)"
    )
    parser.add_argument(
        "--server",
        default="openai",
        help="LLM server (default: openai)"
    )
    parser.add_argument(
        "--model-endpoint",
        default=None,
        help="Optional custom endpoint"
    )
    args = parser.parse_args()

    # call the reviewer directly
    state = {}
    state = code_review_agent(
        state,
        file_path=args.code_file,
        model=args.model,
        server=args.server,
        stop=None,
        model_endpoint=args.model_endpoint
    )

    # print ONLY the JSON feedback
    print(state.get("review_comments", ""))

if __name__ == "__main__":
    main()

# app/app.py

import argparse
from agents.pipeline import pipeline_agent

def main():
    parser = argparse.ArgumentParser(description="Chunked code‐review pipeline (direct)")
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

    # Build up the initial state
    state = {"code_file": args.code_file}

    # Run your entire pipeline in one shot
    final_state = pipeline_agent(
        state,
        model=args.model,
        server=args.server,
        stop=None,
        model_endpoint=args.model_endpoint
    )

    # DEBUG: uncomment to see all keys in the final state
    # print("FINAL STATE:", final_state)

    # Print exactly the merged JSON (no blank lines)
    print(final_state.get("review_comments", ""))

if __name__ == "__main__":
    main()

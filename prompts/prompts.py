# prompts/prompts.py

code_review_prompt_template = """You are a senior software engineer. Review the following Python code chunk and output **only** a JSON object with a single key "issues" whose value is a list of zero-or-more issue objects.
Each issue object must have:
- "line": integer line number
- "issue": string describing the problem
- "severity": one of "low", "medium", or "high"

Do **not** include any prose or markdown—emit exactly:

```json
{{
  "issues": [
    {{ "line": 10, "issue": "...", "severity": "medium" }},
    ...
  ]
}}
Here is the code to review:
{code}
```"""

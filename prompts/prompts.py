# prompts/prompts.py

code_review_prompt_template = """You are a senior software engineer. Review the following Python code and provide:

1. Top 3 issues: one-sentence summary each.
2. Line-by-line comments in JSON:
   [
     {{ "line": 10, "issue": "...", "severity": "low|medium|high" }},
     {{ "line": 20, "issue": "...", "severity": "low|medium|high" }},
     {{ "line": 30, "issue": "...", "severity": "low|medium|high" }}
   ]
3. Overall score out of 5 and a one-sentence improvement suggestion.

```python
{code}
```"""

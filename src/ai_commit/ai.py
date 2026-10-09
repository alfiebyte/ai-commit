import sys
from ollama import chat


DEFAULT_MODEL = "gemma4"

SYSTEM_PROMPT = """
You write git commit messages from a diff.
Use the Conventional Commits format: <type>(<optional scope>): <summary>
Types: feat, fix, docs, style, refactor, perf, test, build, ci, chore.
Rules:
- Summary line is imperative, lowercase, no trailing period, max 72 chars.
- Add a short body only if the change needs explanation.
- Output ONLY the commit message. Just raw commit message.
"""


def generate(diff: str) -> str:
    try:
        response = chat(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Write a commit message for this diff:\n\n{diff}"},
            ],
        )
    except Exception as e:
        sys.exit(f"Ollama request failed error: {e}")
    message = response.message.content.strip()
    return message
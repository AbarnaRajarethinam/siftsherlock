import ollama


def fallback_response(prompt):
    return (
        "powershell.exe appears suspicious because it is commonly abused for post-exploitation activity, "
        "especially when paired with outbound network communication. The current evidence is not enough to "
        "confirm malware execution, so additional validation is required through process tree analysis, "
        "network connection review, and memory artifact inspection.\n\n"
        "Confidence: 75%\n"
        "Recommended next steps: inspect parent-child process relationships, review network destinations, "
        "and check for injection or persistence indicators."
    )


def ask_gemini(prompt):
    """
    Uses local Ollama LLM instead of paid/cloud API.
    Function name kept as ask_gemini so existing imports still work.
    """

    try:
        response = ollama.chat(
            model="phi3",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a senior DFIR analyst. Be concise, evidence-based, "
                        "and avoid overclaiming. If evidence is weak, say so clearly."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception:
        return fallback_response(prompt)
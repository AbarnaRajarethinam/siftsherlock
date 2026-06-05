import subprocess


def check_ollama_model(model_name="phi3"):
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True
        )

        return model_name in result.stdout

    except Exception:
        return False
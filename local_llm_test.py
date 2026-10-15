
import requests

def ask_local_llm(prompt: str) -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3.5:2b",
            "prompt": prompt,
            "stream": False,
            "think": False,
            "options": {
                "num_ctx": 2048,
                "num_predict": 120,
            },
        },
        timeout=600,
    )

    response.raise_for_status()
    result = response.json()

    return result["response"]


answer = ask_local_llm(
    "Explain RAG in two simple sentences."
)

print("\nLOCAL MODEL RESPONSE:\n")
print(answer)

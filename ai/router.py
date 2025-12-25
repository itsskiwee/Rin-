import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1"

SYSTEM_PROMPT = """You are a function router.
Return ONLY raw JSON.
No explanations.
No comments.
No markdown.
No extra fields.

Valid outputs:
{"command":"time"}
{"command":"date"}
{"command":"weather","city":"<city>"}
"""

def route(user_text: str) -> dict:
    payload = {
        "model": MODEL,
        "prompt": SYSTEM_PROMPT + "\nUser: " + user_text,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload).json()
    return json.loads(response["response"])

if __name__ == "__main__":
    text = input(">> ")
    print(route(text))











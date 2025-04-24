from openai import OpenAI
import requests

client = OpenAI(api_key="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")


def ask_chatgpt_obsolete(error_info):
    prompt = f"""
    I've got the following error in a program:
    ---
    Type: {error_info['type']}
    Message: {error_info['message']}
    Traceback:
    {error_info['traceback']}
    ---
    Please:
    1. Explain the likely root cause.
    2. Suggest possible resolutions.
    """

    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content

def ask_chatgpt(prompt: str):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "phi3",  # or whichever model you downloaded
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json().get("response", "No response from model.")
    except requests.RequestException as e:
        return f"Local AI error: {e}"
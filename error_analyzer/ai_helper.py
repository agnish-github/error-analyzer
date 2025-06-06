from openai import OpenAI
import requests

## If using ChatGPT, uncomment and update the api_key with your openAI api key. Then change the function name from ask_chatgpt_obsolete to ask_chatgpt.
## Similarly, rename the 2nd function below from ask_chatgpt to ask_chatgpt_obsolete if you are using Locally running LLMs
client = OpenAI(api_key="<<your-openai-api-key-here>>")

def ask_chatgpt_alt(error_info):
    ## This function is for making requests to ChatGPT
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
    ## This function is to make requests to the locally running LLM Model
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
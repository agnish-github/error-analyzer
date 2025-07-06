import requests

payload = {
    "model": "phi3",  # Update this if your actual model has a tag like phi3:instruct
    "prompt": "Explain the concept of virtual environments in Python.",
    "stream": False
}

response = requests.post("http://localhost:11434/api/generate", json=payload)

print("Status:", response.status_code)
print("Response:", response.text)
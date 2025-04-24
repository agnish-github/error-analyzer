## In my first version of this code, I tried working with chatGPT using their token. However, I faced this error:

## openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information 
## on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

## This left me with just 1 option if I wanted to run this application for free: run a local LLM server that can be accessed through an API on localhost. 

curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3

# ### llama3 is quite large. So on systems running low configurations phi3 & tinydolphin can be used as they are tiny, fast, and still 
# ### surprisingly good at basic analysis, explanations, and summaries.

# ollama run phi3
## ollama rm phi3
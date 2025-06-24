from google import genai
from google.genai import types
import requests

#You will need Deepinfra and Gemini's API keys. Unless, you have another method
#Deepinfra is for both Mistral and Meta models
Deepinfra_api = "your_api_key"
client = genai.Client(api_key = "Your_gemini_api_key") #You will need the Gemini API key via google-genai client

# Function works to query the Mistral AI model via Deepinfra API
#It created to transfer a question and context, epecting a short, specific answer.
def questioning_mistral(qa: str, context: str):
    source = "https://api.deepinfra.com/v1/openai/chat/completions"
    h = {
        "Authorization": f"Bearer {Deepinfra_api}",
        "Content-Type": "application/json"
    }
    prompt = f"Please answer the following question using only context. The answer must be very short and specific.\n\nContext:\n{context}\n\nQuestion: {qa}"
    load = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "You are an assistant. Provide short answer, specific answer using data from the context."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 200
    }
    response = requests.post(source, headers = h, json = load)
    return response.json()['choices'][0]['message']['content'].strip()

def questioning_meta(qa: str, context: str):
    source = "https://api.deepinfra.com/v1/openai/chat/completions"
    h = {
        "Authorization": f"Bearer {Deepinfra_api}",
        "Content-Type": "application/json"
    }
    prompt = f"Please answer the following question using only the context. The answer must be very short and specific.\n\nContext:\n{context}\n\nQuestion: {qa}"
    load = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {"role": "system", "content": "You are an assistant. Provide short answer, specific answer using data from the context."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 200
    }
    response = requests.post(source, headers = h, json = load)
    return response.json()['choices'][0]['message']['content'].strip()

def questioning_gemini(qa: str, context: str):
    prompt = f"Please answer the following question using only the context. The answer must be very short and specific.\nContext:\n{context}\n\nQuestion: {qa}"
    response = client.models.generate_content (
        model = "gemini-2.0-flash",
        contents = prompt,
        config = types.GenerateContentConfig (
            temperature = 0.3,
            max_output_tokens = 200
        )
    )
    return response.text.strip()
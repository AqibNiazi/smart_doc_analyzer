import time
import requests
from openai import OpenAI
from .chunking import chunk_text


# ---- Groq API (OpenAI-compatible) ----
def call_groq(prompt, api_key, model="llama-3.3-70b-versatile", temperature=0.2):
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful summarizer."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )

    return response.choices[0].message.content.strip()


# ---- Hugging Face Inference API ----
def call_huggingface(prompt, api_key, model="facebook/bart-large-cnn"):
    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 200}}

    r = requests.post(url, headers=headers, json=payload)

    # Handle non-JSON errors (like 503 / HTML error pages)
    try:
        data = r.json()
    except ValueError:
        raise ValueError(f"❌ Non-JSON response from Hugging Face: {r.text}")

    # Successful response
    if isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
        return data[0]["generated_text"].strip()
    elif "error" in data:
        raise ValueError(f"❌ Hugging Face API Error: {data['error']}")
    else:
        raise ValueError(f"❌ Unexpected Hugging Face response: {data}")


# ---- Summarizer Flow ----
def summarize_document(text, backend, api_key):
    summaries = []

    for chunk in chunk_text(text):
        prompt = f"Summarize the following:\n\n{chunk}"

        if backend == "grok":
            s = call_groq(prompt, api_key)
        else:
            s = call_huggingface(prompt, api_key)

        summaries.append(s)
        time.sleep(0.5)  # avoid hitting rate limits

    # Merge summaries into one final summary
    final_prompt = "Combine these summaries into a cohesive document summary:\n\n" + "\n".join(summaries)

    return call_groq(final_prompt, api_key) if backend == "grok" else call_huggingface(final_prompt, api_key)

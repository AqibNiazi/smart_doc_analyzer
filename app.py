import os
import streamlit as st
from dotenv import load_dotenv

# Import utilities
from utils.extract_text import extract_text
from utils.summarizer import summarize_document
from utils.tts import text_to_mp3_bytes

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Smart Document Analyzer", layout="wide")
st.title("📄 Smart Document Analyzer")

# Sidebar
with st.sidebar:
    st.header("Settings")
    backend = st.selectbox("LLM Backend", ["grok", "huggingface"])

    if backend == "grok":
        default_key = os.getenv("XAI_API_KEY", "")
    else:
        default_key = os.getenv("HUGGINGFACE_API_KEY", "")

    api_key = st.text_input("API Key", value=default_key, type="password")

    lang = st.selectbox("Audio Language", ["en", "es", "fr", "de"])

# File uploader
uploaded_file = st.file_uploader("Upload document", type=["pdf", "docx", "txt"])
if not uploaded_file:
    st.stop()

# Extract text
raw_text = extract_text(uploaded_file)
if not raw_text:
    st.error("No text found in document")
    st.stop()

st.success("Text extracted successfully!")
st.text_area("Preview (first 2000 chars)", raw_text[:2000], height=200)

# Summarize
if st.button("Generate Summary"):
    summary = summarize_document(raw_text, backend=backend, api_key=api_key)
    st.subheader("📝 Summary")
    st.write(summary)

    

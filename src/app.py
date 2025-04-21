import streamlit as st
import httpx
import json
import tempfile
from extract_pdf import extract_with_pymupdf

st.set_page_config(page_title="Chat To PDFs", layout="centered")
st.title("🧠 Local LLM Assistant to Chat with PDFs")

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Settings")
    model_name = st.selectbox("Choose Model", ["gemma:2b", "llama3"])
    # fastapi_url = st.text_input("FastAPI URL", "http://localhost:8000/ask")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    max_tokens = st.slider("Max Tokens", 64, 1024, 256)
    uploaded_file = st.file_uploader("📁 Upload PDF file", type=["pdf"])

# Main area - extract and display PDF text
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    try:
        extracted_text = extract_with_pymupdf(tmp_file_path)
        st.text_area("📄 Extracted Text", extracted_text, height=300)
    except Exception as e:
        st.error(f"Failed to extract text: {e}")

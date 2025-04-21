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
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    max_tokens = st.slider("Max Tokens", 64, 1024, 256)
    uploaded_file = st.file_uploader("📁 Upload PDF file", type=["pdf"])

# Initialize placeholders
extracted_text = ""
llm_response = ""

# Upload + extract
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name
    try:
        extracted_text = extract_with_pymupdf(tmp_file_path)
    except Exception as e:
        st.error(f"Failed to extract text: {e}")

# Session state for chat-like flow
if "llm_output" not in st.session_state:
    st.session_state.llm_output = ""

# Display LLM response on top
if st.session_state.llm_output:
    st.markdown("### 🤖 Assistant's Response")
    st.text_area("Output", value=st.session_state.llm_output, height=250, label_visibility="collapsed")

# Prompt input at bottom
prompt = st.text_area("💬 Enter your prompt", height=68)
if st.button("Send"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            # For now, fake response — you'd call FastAPI here
            response = f"(Pretend LLM says something clever about your PDF: {prompt})"
            st.session_state.llm_output = response

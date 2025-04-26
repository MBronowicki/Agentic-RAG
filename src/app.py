# app.py

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LLAMA_HOST"] = os.getenv("LLAMA_HOST", "http://localhost:11434")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

# Suppress logging & warnings
import warnings
import logging
warnings.filterwarnings("ignore")
logging.getLogger('streamlit').setLevel(logging.CRITICAL)

import streamlit as st
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from indexer import FaissIndexer
from retrievers import SimpleRetriever
from query_llm import LLMChat
from pathlib import Path
import tempfile

st.set_page_config(page_title="Vector Store Builder", layout="wide")

SUPPORTED_TYPES = {
    ".txt": TextLoader,
    ".pdf": PyPDFLoader,
}

# 🧠 Utility to load docs from uploaded files
def load_documents(files):
    docs = []
    for file in files:
        suffix = Path(file.name).suffix
        if suffix not in SUPPORTED_TYPES:
            st.warning(f"⚠️ Unsupported file type: {file.name}")
            continue
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(file.getbuffer())
                loader = SUPPORTED_TYPES[suffix](tmp.name)
                docs.extend(loader.load())
        except Exception as e:
            st.error(f"❌ Failed to process {file.name}: {e}")
    return docs

@st.cache_resource
def get_indexer():
    return FaissIndexer()

@st.cache_resource
def build_vector_store(_docs):
    indexer = get_indexer()
    return indexer.build_vectorstore(_docs)

# Sidebar – Settings
with st.sidebar:
    st.header("⚙️ Settings")
    model_name = st.selectbox("Choose Model", ["gemma:2b"])
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    max_tokens = st.slider("Max Tokens", 64, 2024, 700)

    st.title("📚 Upload Files")
    uploaded_files = st.file_uploader("Upload .pdf and .txt files", type=["pdf", "txt"], accept_multiple_files=True)

    if uploaded_files and st.button("🔍 Build Vector Store"):
        with st.spinner("Embedding and indexing documents..."):
            docs = load_documents(uploaded_files)
            if docs:
                st.session_state.vs = build_vector_store(docs)
                st.session_state.vs_ready = True
                st.success(f"✅ Vector store built. Documents loaded: {len(docs)}")
            else:
                st.warning("⚠️ No valid documents to process.")

# Main - Query Interface
st.title("🔍 Query the Vector Store")

if st.session_state.get("vs_ready"):
    user_query = st.text_input("Enter your query:", key="query_input")

    if user_query:
        with st.spinner("🔍 Retrieving relevant chunks..."):
            retriever = SimpleRetriever(vectorstore=st.session_state.vs, query=user_query, k=6)
            retrieved_docs = retriever.get_chunks_from_vs()

        if not retrieved_docs:
            st.warning("⚠️ No relevant chunks found!")
        else:
            chunks = "\n\n".join([doc.page_content for doc in retrieved_docs if doc.page_content])
            st.subheader("📄 Retrieved Chunks")
            for i, doc in enumerate(retrieved_docs):
                st.markdown(f"**Chunk {i+1}:**")
                st.write(doc.page_content)

            llm = LLMChat()
            with st.spinner("🤖 Generating response..."):
                response = llm.ask_gemma(user_query, chunks)

            if not response:
                st.warning("⚠️ No response from the LLM!")
            else:
                st.subheader("🤖 LLM Response")
                st.text_area("LLM Response", value=response, height=400)
else:
    st.info("📂 Please upload and build a vector store first.")

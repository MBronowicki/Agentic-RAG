import os
from dotenv import load_dotenv
load_dotenv()
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

import streamlit as st
import asyncio
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
    # Add more if needed
}

# 🧠 Utility to load docs from uploaded files
def load_documents(files):
    docs = []
    for file in files:
        file_suffix = Path(file.name).suffix
        if file_suffix not in SUPPORTED_TYPES:
            st.warning(f"⚠️ Unsupported file type: {file.name}")
            continue

        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=file_suffix) as tmp_file:
                tmp_file.write(file.getbuffer())
                tmp_file_path = tmp_file.name

            loader_class = SUPPORTED_TYPES[file_suffix]
            loader = loader_class(tmp_file_path)
            docs.extend(loader.load())
        except Exception as e:
            st.error(f"❌ Failed to process {file.name}: {e}")
    return docs

# Initialize vector store
vs = None

with st.sidebar:
    # 📤 Upload section
    st.header("⚙️ Settings")
    model_name = st.selectbox("Choose Model", ["gemma:2b", "llama3"])
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    max_tokens = st.slider("Max Tokens", 64, 2024, 700)

    st.title("📚 Upload Files and Build a Vector Store")
    uploaded_files = st.file_uploader(
        "Upload .pdf and .txt files", type=["pdf", "txt"], accept_multiple_files=True
    )
    
    # 🧠 Process documents
    if uploaded_files and st.button("🔍 Build Vector Store"):
        with st.spinner("Loading and embedding documents..."):
            docs = load_documents(uploaded_files)
            if docs:
                faiss_indexer = FaissIndexer()
                vs = faiss_indexer.build_vectorstore(docs)
                st.success(f"✅ Vector store built and saved. Documents loaded: {len(docs)}")
            else:
                st.warning("⚠️ No valid documents to process.")

st.title("🔍 Query the Vector Store")
user_query = st.text_input("Enter your query:")

if vs and user_query:
    # Debugging: Check if vector store is properly initialized
    st.write("Vectorstore is initialized.")
    
    # Get the relevant chunks from the vector store
    retriever = SimpleRetriever(vectorstore=vs, query=user_query, k=4)
    retrieved_docs = retriever.get_chunks_from_vs()
    
    # Debugging: Check if we retrieved any chunks
    if not retrieved_docs:
        st.warning("⚠️ No relevant chunks found!")
    else:
        st.write(f"Retrieved {len(retrieved_docs)} chunks.")

    chunks = "\n\n".join([doc.page_content for doc in retrieved_docs if doc.page_content])

    # Show retrieved chunks in the main area
    st.subheader("Retrieved Chunks")
    for i, doc in enumerate(retrieved_docs):
        st.markdown(f"**Chunk {i+1}:**")
        st.write(doc.page_content)

    # Handle LLM response
    llm = LLMChat(model=model_name, temperature=temperature, max_tokens=max_tokens)
    response = llm.ask_gemma(user_query, chunks)
    
    # Debugging: Ensure we get an LLM response
    if not response:
        st.warning("⚠️ No response from the LLM!")
    else:
        st.subheader("🤖 LLM Response")
        st.text_area("LLM Response", response, height=200)

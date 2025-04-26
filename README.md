# 🧠 **Vector Store Querying with Ollama**

This project provides a **Vector Store** built using **LangChain**, integrated with **Ollama** to query models like **Gemma** (2B). With this stack, you can upload documents (PDFs and TXT), build a vector store, and query it using a language model for intelligent responses. 

---

## 🚀 **Getting Started**

Before running the app, ensure you have the following:

1. **Ollama CLI** to run models like **Gemma** locally.
2. **Docker** installed on your machine.
3. **Python 3.10 or 3.11** (recommended).

---

## 🛠️ **Installation Steps**

### 1. Install **Ollama CLI**:

First, you need to install **Ollama CLI** to run models locally.

#### **Install Ollama CLI**:
- Go to the [Ollama github website](https://github.com/ollama/ollama) and follow the installation instructions for your OS (Windows, macOS, or Linux).
  
For example, on macOS:
```bash
  brew install ollama
```

- After installation, verify that **Ollama CLI** is working:
```bash
    ollama --version
```

### 2. Pull the model:
Pull the model you want to use (currently **Gemma**):
```bash
    ollama pull gemma:2b
```
⚠️ Important: Currently only **gemma:2b** is available for use in this pipeline.

You can then list models:
```bash
    ollama list
```

### 3. Run Docker image
After pulling the model, you can start the application using Docker Compose:

```bash
    docker compose up -d
```

## 🎯 Using the Application

### 1. Upload Documents:
Once the app is running, upload `.pdf` or `.txt` files. These files will be processed to build a vector store.
### 2. Adjust Model Parameters:
- You can adjust parameters such as:
- Model selection (currently Gemma)
- Temperature
- Maximum tokens

to customize the behavior of the response.
### 3. Query the Vector Store:
After uploading documents, you can enter a query. The app will retrieve the relevant chunks of text from the vector store and use the model (e.g., Gemma) to generate a response based on the query.

## 🔧 Conclusion
This stack enables you to quickly build and query a Vector Store using **LangChain**, **Ollama's LLMs (Gemma)**, and **Streamlit** for an intuitive interface. By using Docker Compose, I make it easy to deploy and run the app locally.

## 🌟 Future Improvements (Ideas)
Here are some ideas for enhancing this project further:

- Improve Text Preprocessing:

    - Clean and split extracted text more intelligently (e.g., removing special characters, better sentence splitting).

- Use Larger Models:

    - Upgrade to larger models like Llama 3 (7B, 13B) for better context understanding and richer answers.

- Increase Context Window:

    - Switch to models with a larger context window to improve long-document comprehension.

- Build a More Advanced RAG System:

    - Implement Self-Reflective RAG, Re-ranking, or Multi-hop Retrieval for even better answers.

- Experiment with Chunk Sizes and Splitting Techniques:

    - Tune the chunk sizes and try advanced splitting (e.g., semantic splitting) to improve retrieval precision.

Enjoy querying your vector store! 😎
<p align="center"> <img src="https://img.shields.io/badge/Docker-🐳-blue" alt="Docker Badge" /> <img src="https://img.shields.io/badge/LangChain-🔗-yellowgreen" alt="LangChain Badge" /> <img src="https://img.shields.io/badge/Ollama-🤖-lightgrey" alt="Ollama Badge" /> <img src="https://img.shields.io/badge/Python-3.10/3.11-blueviolet" alt="Python Badge" /> </p>

# 🧠 **Vector Store Querying with Ollama Run Locally**


This project provides a **Vector Store** built using **LangChain**, integrated with **Ollama** to query models like **Gemma** (2B). With this stack, you can upload documents (PDFs), build a vector store, and query it using a language model for intelligent responses. 

---

## 📑 **Table of Contents**
- [🚀 Getting Started](#getting-started)
- [🛠️ Installation Steps](#installation-steps)
  - [1. Install Ollama CLI](#install-ollama-cli)
  - [2. Pull the Model](#pull-the-model)
  - [3. Run Docker Image](#run-docker-image)
- [🎯 Using the Application](#using-the-application)
- [🌟 Future Improvements](#future-improvements-ideas)
- [🔧 Conclusion](#conclusion)

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
- Go to the [Ollama GitHub website](https://github.com/ollama/ollama) and follow the installation instructions for your OS (Windows, macOS, or Linux).
  
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

## 🖥️ Using the Application

### 1. 📤 Upload Documents:
Once the app is running, upload `.pdf` files. These files will be processed to build a vector store.
### 2. ⚙️ Adjust Model Parameters:
You can adjust parameters such as:
- 🤖 Model selection (currently Gemma)
- 🌡️ Temperature
- 🔢 Maximum tokens

While you can modify these settings to fine-tune the behavior of the responses, keep in mind that since this system uses a smaller LLM, the impact of these adjustments may be less noticeable compared to larger models. Nevertheless, experimenting with them can still help improve the generated output within the system’s constraints.

### 3. 🔍 Query the Vector Store:
After uploading documents, you can enter a query. The app will retrieve the relevant chunks of text from the vector store and use the model (e.g., Gemma) to generate a response based on the query.


## 🌟 Future Improvements (Ideas)

Here are some ideas for enhancing this project further:

- 🌱 **Improve Text Preprocessing** - Clean and split extracted text more intelligently (e.g., removing special characters, better sentence splitting).

- 🧠 **Upgrade to Larger Models** - Switch to larger models like **Llama 3** (7B, 13B) for better context understanding, richer answers, and to improve long-document comprehension with a larger context window.

- 🔧 **Build a More Advanced RAG System**  
  Implement techniques like:
  - 🤖 **Self-Reflective RAG** (model reflects on retrieval).
  - 🔍 **Re-ranking retrieved chunks** (to prioritize the most relevant).
  - 🔄 **Multi-hop Retrieval** (retrieve-answer-retrieve for complex queries).

- 🧩 **Experiment with Chunk Sizes and Splitting Techniques** - Tune the chunk sizes and try advanced splitting (e.g., semantic splitting) to improve retrieval precision.

- ⚡ **Introduce Async Processing** - Refactor critical parts (like LLM querying and file loading) to **async/await** to handle multiple user queries more efficiently, especially for scaling.

- 🖥️ **Backend API Separation**  
  Optionally split the app into:
  - ⚙️ **FastAPI backend** (async, scalable).
  - 🎨 **Streamlit or React frontend** (for a modern, user-friendly UI).


## 🔧 Conclusion
This stack allows you to quickly build and query a Vector Store using **LangChain**, **Ollama's LLMs (Gemma 2B)**, and **Streamlit** for an intuitive interface. By creating a **Docker image** and leveraging **Docker Compose**, I've streamlined the process of deploying and running the app locally, making it simple to use without external dependencies.

---

🚀 Enjoy building and querying your vector store! Happy experimenting! 😎
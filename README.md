# 🧠 **Vector Store Querying with Ollama**

This project provides a **Vector Store** built using **LangChain**, integrated with **Ollama** to query models like **Gemma** (2B) and **Llama3**. With this stack, you can upload documents (PDFs and TXT), build a vector store, and query it using a language model for intelligent responses. 

---

## 🚀 **Getting Started**

Before running the app, ensure you have the following:

1. **Ollama CLI** to run models like **Gemma** and **Llama** locally.
2. **Docker** installed on your machine.
3. **Python 3.10 or 3.11** (recommended).

---

## 🛠️ **Installation Steps**

### 1. Install **Ollama CLI**:

First, you need to install **Ollama CLI** to run models like **Gemma** and **Llama** locally.

#### **Install Ollama CLI**:
- Go to the [Ollama github website](https://github.com/ollama/ollama) and follow the installation instructions for your OS (Windows, macOS, or Linux).
  
For example, on macOS:
```bash
  brew install ollama
```

- After installation, veryfy that Ollama CLI is working:
```bash
    ollama --version
```

### 2. Pull the model:
Run the following command to pull the model you want to use (e.g., **Gemma**):
```bash
    ollama pull gemma:2b
```
You can then run it with:
```bash
    ollama run gemma:2b
```

Exit the shell, then you can list running models by using:
```bash
    ollama ps
```

### 3. Run Docker image
After pulling the model and running it, you can now start the application using Docker Compose:

```bash
    docker compose up
```

## 🎯 Using the Application

### 1. Upload Documents:
Once the app is running, upload `.pdf` or `.txt` files. These files will be processed to build a vector store.
### 2. Query the Vector Store:
After uploading documents, you can enter a query. The app will retrieve the relevant chunks of text from the vector store and use Gemma or Llama3 to generate a response based on the query.
### 3. Adjust Model Parameters:
You can select the model (either Gemma or Llama), set the temperature, and adjust the maximum tokens to customize the behavior of the response.

## ⚙️ Troubleshooting
- **Ollama Not Found**: Ensure that Ollama CLI is installed correctly and is in your PATH.
- **Memory Issues**: The Llama3 model requires significant memory. If your system has insufficient RAM, consider using the Gemma model.
- **Permissions**: If you run into permission issues while using Docker, try using sudo or ensure your Docker user has proper permissions.

## 🔧 Conclusion
This stack enables you to quickly build and query a Vector Store using LangChain, Ollama's LLMs (Gemma and Llama), and Streamlit for an intuitive interface. By using Docker Compose, I make it easy to deploy and run the app locally.

Enjoy querying your vector store! 😎
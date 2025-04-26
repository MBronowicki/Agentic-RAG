import ollama
from langchain.prompts import PromptTemplate

def ask_gemma(query: str, model: str = "gemma:2b", temperature: float = 0.6, max_tokens: int = 256) -> str:
    try:
        messages = [
            {"role": "system", "content": system_template.format()},
            {"role": "user", "content": user_template.format(query=query)}
        ]

        response = ollama.chat(
            model=model,
            messages=messages,
            options={
                "temperature": temperature,
                "num_predict": max_tokens
            }
        )

        return response["message"]["content"].strip()

    except Exception as e:
        print(f"❌ Error: {e}")
        return "An error occurred while processing the request."


if __name__ == "__main__":

    # Define the System and User Prompts using LangChain
    # Prompt templates
    system_prompt = """You are a helpful assistant. Answer clearly, concisely, and in plain natural language."""

    user_prompt = """{query}"""

    # LangChain Prompt Template
    system_template = PromptTemplate(template=system_prompt, input_variables=[])
    user_template = PromptTemplate(template=user_prompt, input_variables=["query"])

    # Example usage
    query = "What is RAG system in AI"
    response = ask_gemma(query)
    print(response)

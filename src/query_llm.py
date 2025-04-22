import ollama
from langchain.prompts import PromptTemplate


class LLMChat:
    def __init__(
            self, model: str = "gemma:2b", temperature: float = 0.6, max_tokens: int = 1024
            ):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def ask_gemma(self, query: str, chunks: str) -> str:
        # Define the System and User Prompts using LangChain
        # Prompt templates
        system_prompt = (
        "You are a knowledgeable and helpful assistant. "
        "Use the retrieved information to provide accurate, concise, and easy-to-understand answers. "
        "If the information is not available or unclear, state that honestly."
    )

        user_prompt = """
        Answer the following question using the provided information.

        ### User Question:
        {query}

        ### Retrieved Information:
        {chunks}

        Only use the retrieved information to answer. If the answer isn't found in the context, say so.
        """

        # LangChain Prompt Template
        system_template = PromptTemplate(template=system_prompt, input_variables=[])
        user_template = PromptTemplate(template=user_prompt, input_variables=["query", "chunks"])

        try:
            messages = [
                {"role": "system", "content": system_template.format()},
                {"role": "user", "content": user_template.format(query=query, chunks=chunks)}
            ]

            response = ollama.chat(
                model=self.model,
                messages=messages,
                options={
                    "temperature": self.temperature,
                    "num_predict": self.max_tokens
                }
            )

            return response["message"]["content"].strip()

        except Exception as e:
            print(f"❌ Error: {e}")
            return "An error occurred while processing the request."


if __name__ == "__main__":
    # Example usage
    query = "What is RAG system in AI"
    llm = LLMChat
    response = llm.ask_gemma(query)
    print(response)

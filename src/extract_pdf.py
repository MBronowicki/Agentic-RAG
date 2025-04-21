# This script exctract text from pdf for our RAG system
import fitz
import re
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def extract_with_pymupdf(path: str) -> str:
    """Function extract text from pdf (text-based, not scanned images)"""
    doc = fitz.open(path)

    text = ""
    for page in doc:
        text += page.get_textpage().extractText()
    doc.close()

    # Remove References section and everything after
    text = re.split(r'\bReferences\b', text, flags=re.IGNORECASE)[0].strip()
    return text



if __name__ == "__main__":

    pdf_path = "../data/Retrieval-Augmented Generation for Large Language Models- A Surveypdf.pdf"

    text = extract_with_pymupdf(pdf_path)
    print(text)

    # # Load PDF using LangChain
    # loader = PyMuPDFLoader(pdf_path)
    # docs = loader.load()
    # for doc in docs:
    #     print(f"\n--- Page: {doc.metadata["page"]} ---\n")
    #     print(doc.page_content)
    

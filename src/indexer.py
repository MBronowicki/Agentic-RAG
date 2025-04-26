# indexer.py

import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List
from base_models import IndexerConfig

class FaissIndexer:
    def __init__(self):
        self.config = IndexerConfig()
        self.embeddings = HuggingFaceEmbeddings(model_name=self.config.embedding_model)

    def chunk_documents(self, _docs: List[Document]) -> List[Document]:
        """Splits documents into smaller chunks"""
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.config.chunk_size,
            chunk_overlap=self.config.chunk_overlap
        )
        return splitter.split_documents(_docs)
    
    def build_vectorstore(self, _docs: List[Document], save: bool = True) -> FAISS:
        """Builds and store embedded text chunks in vector store """
        chunks  = self.chunk_documents(_docs)
        vectorstore = FAISS.from_documents(chunks, self.embeddings)
        if save:
            vectorstore.save_local(self.config.db_path)
        return vectorstore
    
    def load_vectorstores(self) -> FAISS:
        """Not implemented yet"""
        return FAISS.load_local(self.config.db_path, self.embeddings)


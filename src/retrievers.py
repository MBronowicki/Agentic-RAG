# Retrievers.py

class SimpleRetriever:
    def __init__(self, vectorstore, query, k=3):
        self.vectorstore = vectorstore
        self.query = query
        self.k = k
    
    def get_chunks_from_vs(self):
        retriever = self.vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": self.k,
                           "lambda_mult": 0.65}
        )
        results = retriever.invoke(self.query)
        return results

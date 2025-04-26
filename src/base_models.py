# base_models.py

from pydantic import BaseModel, Field

class IndexerConfig(BaseModel):
    embedding_model: str = Field(default="all-MiniLM-L6-v2", description="HuggingFace model name")
    chunk_size: int = Field(default=1000, ge=100, le=1024, description="Chunk size for splitting text")
    chunk_overlap: int = Field(default=50, ge=0, le=1000, description="Overlap between chunks")
    db_path: str = Field(default="faiss_index", description="Path to save/load FAISS index")
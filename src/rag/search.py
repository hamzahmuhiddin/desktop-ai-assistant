from src.rag.vector_store import VectorStore
from src.rag.embedder import TextEmbedder


class SemanticSearch:
    """
    Semantic search module untuk mencari dokumen relevan.
    
    Returns:
        Dict dengan keys:
        - documents: List of text chunks
        - distances: List of distance scores (relevance)
        - metadatas: List of metadata dicts
    """

    def __init__(self):
        self.embedder = TextEmbedder()
        self.vector_store = VectorStore()

    def search(self, question: str, top_k: int = 5) -> dict:
        """
        Search untuk dokumen relevan dengan pertanyaan.
        
        Args:
            question: User query
            top_k: Jumlah top results (default: 5)
            
        Returns:
            Dict dengan documents, distances, dan metadatas
        """
        # Embed query
        query_embedding = self.embedder.encode([question])[0]

        # Search di vector DB
        results = self.vector_store.search(query_embedding, top_k)

        return results
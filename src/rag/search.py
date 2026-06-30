from src.rag.vector_store import VectorStore
from src.rag.embedder import TextEmbedder


class SemanticSearch:

    def __init__(self):

        self.embedder = TextEmbedder()

        self.vector_store = VectorStore()

    def search(self, question, top_k=5):

        query_embedding = self.embedder.encode([question])[0]

        results = self.vector_store.search(
            query_embedding,
            top_k
        )

        return results
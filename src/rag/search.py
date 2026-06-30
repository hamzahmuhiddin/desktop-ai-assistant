import chromadb

from src.rag.embedder import TextEmbedder


class SemanticSearch:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="vector_db")

        self.collection = self.client.get_collection("documents")

        self.embedder = TextEmbedder()

    def search(self, question, top_k=5):

        query_embedding = self.embedder.encode([question])[0].tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results["documents"][0]
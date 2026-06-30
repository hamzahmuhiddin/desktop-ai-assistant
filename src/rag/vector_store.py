import chromadb


class VectorStore:

    def __init__(self, db_path="vector_db"):

        self.client = chromadb.PersistentClient(path=db_path)

        try:
            self.client.delete_collection("documents")
        except:
            pass

        self.collection = self.client.create_collection(
            name="documents"
        )

    def add_documents(self, chunks, embeddings):

        ids = [str(i) for i in range(len(chunks))]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist()
        )

    def search(self, query_embedding, top_k=5):

        result = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k
        )

        return result
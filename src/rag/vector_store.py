import chromadb


class VectorStore:

    def __init__(self, db_path="vector_db"):

        self.client = chromadb.PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_documents(self, chunks, embeddings):

        ids = [str(i) for i in range(len(chunks))]

        metadatas = []

        for i in range(len(chunks)):
            metadatas.append(
                {
                    "chunk_id": i,
                    "source": "PROPOSAL TESIS.pdf"
                }
            )

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

    def search(self, query_embedding, top_k=5):

        return self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k,
            include=[
                "documents",
                "distances",
                "metadatas"
            ]
        )
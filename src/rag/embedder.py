from sentence_transformers import SentenceTransformer


class TextEmbedder:

    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )
        print("Embedding model loaded.")

    def encode(self, chunks):
        return self.model.encode(chunks)
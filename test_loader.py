from src.rag.loader import DocumentLoader
from src.rag.cleaner import TextCleaner
from src.rag.chunker import TextChunker
from src.rag.embedder import TextEmbedder
from src.rag.vector_store import VectorStore

loader = DocumentLoader()
cleaner = TextCleaner()
chunker = TextChunker()
embedder = TextEmbedder()
vector_store = VectorStore()

print("Loading PDF...")

text = loader.load("docs/PROPOSAL TESIS.pdf")

print("Cleaning text...")

clean_text = cleaner.clean(text)

print("Creating chunks...")

chunks = chunker.split(clean_text)

print("Creating embeddings...")

embeddings = embedder.encode(chunks)

print("Saving to ChromaDB...")

vector_store.add_documents(chunks, embeddings)

print("=" * 50)
print("Jumlah Chunk :", len(chunks))
print("Embedding Shape :", embeddings.shape)
print("Saved to ChromaDB :", len(chunks), "documents")
print("=" * 50)
from src.rag.loader import DocumentLoader
from src.rag.cleaner import TextCleaner
from src.rag.chunker import TextChunker
from src.rag.embedder import TextEmbedder
from src.rag.vector_store import VectorStore

print("Loading PDF...")

loader = DocumentLoader()
cleaner = TextCleaner()
chunker = TextChunker()
embedder = TextEmbedder()
store = VectorStore()

text = loader.load("docs/PROPOSAL TESIS.pdf")

print("Cleaning text...")
clean_text = cleaner.clean(text)

print("Creating chunks...")
chunks = chunker.split(clean_text)

print("Creating embeddings...")
embeddings = embedder.encode(chunks)

print("Saving to ChromaDB...")
store.add_documents(chunks, embeddings)

print("=" * 50)
print("Documents :", len(chunks))
print("Done.")
print("=" * 50)
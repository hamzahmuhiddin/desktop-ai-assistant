from src.rag.loader import DocumentLoader
from src.rag.cleaner import TextCleaner
from src.rag.chunker import TextChunker
from src.rag.embedder import TextEmbedder

loader = DocumentLoader()
cleaner = TextCleaner()
chunker = TextChunker()
embedder = TextEmbedder()

text = loader.load("docs/PROPOSAL TESIS.pdf")

clean_text = cleaner.clean(text)

chunks = chunker.split(clean_text)

embeddings = embedder.encode(chunks)

print("=" * 50)
print("Jumlah Chunk :", len(chunks))
print("Embedding Shape :", embeddings.shape)
print("=" * 50)
from src.rag.loader import DocumentLoader
from src.rag.cleaner import TextCleaner
from src.rag.chunker import TextChunker

loader = DocumentLoader()
cleaner = TextCleaner()
chunker = TextChunker()

text = loader.load("docs/PROPOSAL TESIS.pdf")

clean_text = cleaner.clean(text)

chunks = chunker.split(clean_text)

print("=" * 50)
print("Jumlah Chunk :", len(chunks))
print("=" * 50)

for i, chunk in enumerate(chunks[:3]):
    print(f"\n===== CHUNK {i+1} =====\n")
    print(chunk)
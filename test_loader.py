from src.rag.loader import DocumentLoader
from src.rag.cleaner import TextCleaner

loader = DocumentLoader()
cleaner = TextCleaner()

text = loader.load("docs/PROPOSAL TESIS.pdf")

clean_text = cleaner.clean(text)

with open("hasil_bersih.txt", "w", encoding="utf-8") as f:
    f.write(clean_text)

print("=" * 50)
print("Jumlah karakter :", len(clean_text))
print("File hasil_bersih.txt berhasil dibuat.")
print("=" * 50)
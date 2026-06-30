from src.rag.search import SemanticSearch
from src.core.gemini import ask_gemini


class RAGPipeline:

    def __init__(self):
        self.search = SemanticSearch()

    def ask(self, question):

        documents = self.search.search(question)

        print("\n===== HASIL SEARCH =====\n")

        for i, doc in enumerate(documents, 1):
            print(f"\n--- Chunk {i} ---\n")
            print(doc[:500])

        context = "\n\n".join(documents)

        prompt = f"""
Jawablah pertanyaan HANYA berdasarkan konteks berikut.

Jika jawabannya tidak ada di konteks, katakan bahwa informasi tidak ditemukan.

KONTEKS:
{context}

PERTANYAAN:
{question}
"""

        return ask_gemini(prompt)
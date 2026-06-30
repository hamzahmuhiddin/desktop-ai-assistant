from src.core.gemini import ask_gemini
from src.rag.search import SemanticSearch


class RAGPipeline:

    def __init__(self):
        self.search = SemanticSearch()

    def ask(self, question):

        results = self.search.search(question)

        documents = results["documents"][0]
        scores = results["distances"][0]
        metadatas = results["metadatas"][0]

        print("\n===== HASIL SEARCH =====")

        context_docs = []

        for i in range(len(documents)):

            print(f"\n--- Chunk {i+1} ---")
            print("Distance :", scores[i])
            print("Metadata :", metadatas[i])
            print(documents[i][:500])

            context_docs.append(documents[i])

        context = "\n\n".join(context_docs)

        prompt = f"""
Jawablah pertanyaan HANYA berdasarkan konteks berikut.

Jika jawabannya tidak ada di konteks,
katakan "Informasi tidak ditemukan."

====================
KONTEKS
====================

{context}

====================
PERTANYAAN
====================

{question}
"""

        return ask_gemini(prompt)
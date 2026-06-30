from src.core.gemini import ask_gemini
from src.rag.search import SemanticSearch


class RAGPipeline:
    """
    RAG Pipeline dengan quality filtering.
    
    Features:
    - Distance threshold filtering (hanya ambil chunk relevan)
    - Empty context handling (jangan call Gemini jika kosong)
    - Strengthened prompt (instruksi ketat untuk mengurangi hallucination)
    """

    # Configuration
    DISTANCE_THRESHOLD = 1.5  # Chroma distance (lebih rendah = lebih relevan)
    MIN_CONTEXT_CHARS = 100   # Minimum chars untuk valid context

    def __init__(self):
        self.search = SemanticSearch()

    def ask(self, question: str) -> str:
        """
        Process question dengan RAG pipeline.
        
        Returns:
            str: Answer dari Gemini atau "Informasi tidak ditemukan"
        """
        
        # Step 1: Semantic search
        results = self.search.search(question)

        # Step 2: Extract dan filter results
        documents = results["documents"][0]
        distances = results["distances"][0]
        metadatas = results["metadatas"][0]

        # Step 3: Quality filtering - ambil hanya yang relevan
        context_docs = self._filter_by_distance(
            documents, distances, metadatas
        )

        # Step 4: Print debug info
        self._print_search_results(documents, distances, metadatas, context_docs)

        # Step 5: Check if context valid
        if not context_docs:
            return "Informasi tidak ditemukan dalam dokumen."

        # Step 6: Build context
        context = "\n\n".join(context_docs)

        # Step 7: Check context length
        if len(context) < self.MIN_CONTEXT_CHARS:
            return "Informasi tidak ditemukan dalam dokumen."

        # Step 8: Build prompt dengan instruksi ketat
        prompt = self._build_rag_prompt(question, context)

        # Step 9: Call Gemini
        return ask_gemini(prompt)

    def _filter_by_distance(self, documents, distances, metadatas):
        """
        Filter documents berdasarkan distance threshold.
        
        Args:
            documents: List of text chunks
            distances: List of distance scores (dari Chroma)
            metadatas: List of metadata dicts
            
        Returns:
            List of filtered documents that meet threshold
        """
        filtered = []

        for i in range(len(documents)):
            distance = distances[i]
            doc = documents[i]
            
            # Chroma: distance lebih kecil = lebih relevan
            # Threshold 1.5 berarti accept jika distance < 1.5
            if distance < self.DISTANCE_THRESHOLD:
                filtered.append(doc)

        return filtered

    def _print_search_results(self, documents, distances, metadatas, filtered):
        """Debug output - tampilkan hasil search."""
        print("\n" + "=" * 70)
        print("SEMANTIC SEARCH RESULTS")
        print("=" * 70)

        for i in range(len(documents)):
            distance = distances[i]
            metadata = metadatas[i]
            doc = documents[i]
            
            # Mark jika filtered
            status = "✓ USED" if doc in filtered else "✗ FILTERED"

            print(f"\n[Chunk {i + 1}] {status}")
            print(f"Distance: {distance:.4f} (threshold: {self.DISTANCE_THRESHOLD})")
            print(f"Metadata: {metadata}")
            print(f"Preview: {doc[:200]}...")

        print("\n" + "=" * 70)
        print(f"Total chunks: {len(documents)} | Used: {len(filtered)}")
        print("=" * 70 + "\n")

    def _build_rag_prompt(self, question: str, context: str) -> str:
        """
        Build RAG prompt dengan instruksi ketat.
        
        Args:
            question: User question
            context: Retrieved context dari vector DB
            
        Returns:
            Formatted prompt untuk Gemini
        """
        prompt = f"""ANDA ADALAH ASISTEN PENELITIAN YANG ANDAL.

INSTRUKSI KETAT:
1. HANYA gunakan informasi dari KONTEKS di bawah
2. Jika jawaban TIDAK ADA di konteks, katakan: "Informasi tidak ditemukan dalam dokumen"
3. JANGAN mengarang atau assume informasi yang tidak ada
4. Jika pertanyaan ambigu, minta klarifikasi
5. Cantumkan SUMBER dari konteks jika relevan
6. Berikan jawaban yang TERSTRUKTUR dan JELAS

================================================================================
KONTEKS DARI DOKUMEN:
================================================================================

{context}

================================================================================
PERTANYAAN PENGGUNA:
================================================================================

{question}

================================================================================
INSTRUKSI FINAL:
- Jawab berdasarkan konteks SAJA
- Jika tidak ada, katakan "Informasi tidak ditemukan dalam dokumen"
- Berikan jawaban yang RINGKAS tapi LENGKAP
================================================================================

JAWABAN:
"""
        return prompt
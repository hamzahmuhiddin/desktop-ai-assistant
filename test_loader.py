from src.rag.search import SemanticSearch

search = SemanticSearch()

results = search.search(
    "Apa tujuan penelitian ini?"
)

print("=" * 50)

for i, doc in enumerate(results, start=1):

    print(f"\n===== HASIL {i} =====\n")

    print(doc[:500])

print("=" * 50)
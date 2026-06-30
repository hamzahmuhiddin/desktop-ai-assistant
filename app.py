from src.core.assistant import Assistant

ai = Assistant()

print("=" * 50)
print("Desktop AI Assistant")
print("=" * 50)

while True:

    question = input("\nAnda : ").strip()

    if question.lower() == "exit":
        print("Sampai jumpa.")
        break

    if not question:
        print("\nSilakan masukkan pertanyaan.")
        continue

    try:

        answer = ai.ask(question)

        print("\nAI :", answer)

    except Exception as e:

        print("\nERROR :", e)
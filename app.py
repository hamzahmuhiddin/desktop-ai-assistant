from src.core.assistant import Assistant

ai = Assistant()

print("=" * 50)
print("Desktop AI Assistant")
print("=" * 50)

while True:

    question = input("\nAnda : ")

    if question.lower() == "exit":
        print("Sampai jumpa.")
        break

    try:

        answer = ai.ask(question)

        print("\nAI :", answer)

    except Exception as e:

        print("\nERROR :", e)
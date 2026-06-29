from src.core.gemini import GeminiAssistant

assistant = GeminiAssistant()

print("=" * 50)
print("Desktop AI Assistant")
print("=" * 50)

while True:
    question = input("\nAnda : ")

    if question.lower() in ["exit", "quit"]:
        print("Sampai jumpa.")
        break

    try:
        answer = assistant.ask(question)
        print("\nAI :", answer)
    except Exception as e:
        print("\nERROR :", e)
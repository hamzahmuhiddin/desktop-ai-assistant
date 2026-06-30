from src.core.gemini import ask_gemini
from src.core.memory import ConversationMemory


class Assistant:

    def __init__(self):
        self.memory = ConversationMemory()

    def ask(self, question):

        self.memory.add_user(question)

        answer = ask_gemini(
            question,
            history=self.memory.get_history()
        )

        self.memory.add_ai(answer)

        return answer
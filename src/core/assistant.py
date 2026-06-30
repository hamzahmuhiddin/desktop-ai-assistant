from src.rag.pipeline import RAGPipeline
from src.core.memory import ConversationMemory


class Assistant:

    def __init__(self):
        self.memory = ConversationMemory()
        self.rag = RAGPipeline()

    def ask(self, question):

        self.memory.add_user(question)

        answer = self.rag.ask(question)

        self.memory.add_ai(answer)

        return answer
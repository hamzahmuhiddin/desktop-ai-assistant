class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_user(self, message):
        self.history.append({
            "role": "user",
            "parts": [message]
        })

    def add_ai(self, message):
        self.history.append({
            "role": "model",
            "parts": [message]
        })

    def get_history(self):
        return self.history

    def clear(self):
        self.history = []
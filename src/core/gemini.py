from google import genai
from src.config.settings import GEMINI_API_KEY, MODEL_NAME


class GeminiAssistant:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def ask(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text
from google import genai
from src.config.settings import GEMINI_API_KEY, MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt, history=None):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
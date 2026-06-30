from groq import Groq
from google import genai
from src.config.settings import GROQ_API_KEY, GEMINI_API_KEY, GROQ_MODEL, GEMINI_MODEL

groq_client = Groq(api_key=GROQ_API_KEY)
gemini_client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt, history=None):
    """
    Coba Groq dulu (limit lebih longgar).
    Kalau gagal/limit habis, otomatis fallback ke Gemini.
    """
    try:
        response = groq_client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1024,
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"\n[WARNING] Groq gagal ({e}), fallback ke Gemini...\n")

        try:
            response = gemini_client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt
            )
            return response.text

        except Exception as e2:
            return f"Maaf, kedua provider AI sedang tidak tersedia. Error: {e2}"
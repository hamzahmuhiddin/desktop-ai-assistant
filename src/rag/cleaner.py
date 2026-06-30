import re


class TextCleaner:

    def clean(self, text: str) -> str:
        # Hilangkan spasi berlebih
        text = re.sub(r"[ \t]+", " ", text)

        # Gabungkan baris yang hanya terputus karena layout PDF
        text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

        # Maksimal dua newline
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Hilangkan spasi di awal/akhir
        text = text.strip()

        return text
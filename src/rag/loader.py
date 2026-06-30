from pathlib import Path

from pypdf import PdfReader

from docx import Document


class DocumentLoader:

    def load(self, file_path):

        path = Path(file_path)

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            return self._load_pdf(path)

        elif suffix == ".docx":
            return self._load_docx(path)

        elif suffix == ".txt":
            return self._load_txt(path)

        else:
            raise ValueError(f"Format tidak didukung: {suffix}")

    def _load_pdf(self, path):

        reader = PdfReader(path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"

        return text

    def _load_docx(self, path):

        doc = Document(path)

        return "\n".join(
            p.text for p in doc.paragraphs
        )

    def _load_txt(self, path):

        with open(path, "r", encoding="utf-8") as f:
            return f.read()
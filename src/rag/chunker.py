class TextChunker:
    """
    Paragraph-based chunker dengan target size besar.
    
    Menggabungkan paragraf sampai mencapai target_size,
    supaya konteks tidak terlalu terpecah-pecah
    (chunk kecil = konteks hilang, hasil retrieval buruk).
    """

    def __init__(self, target_size=3000):
        self.target_size = target_size

    def split(self, text):
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        chunks = []
        current = ""

        for paragraph in paragraphs:

            if len(current) + len(paragraph) < self.target_size:
                current += paragraph + "\n\n"
            else:
                if current:
                    chunks.append(current.strip())
                current = paragraph + "\n\n"

        if current:
            chunks.append(current.strip())

        return chunks
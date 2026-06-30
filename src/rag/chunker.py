class TextChunker:

    def split(self, text):

        paragraphs = text.split("\n\n")

        chunks = []

        current = ""

        for paragraph in paragraphs:

            if len(current) + len(paragraph) < 1200:

                current += paragraph + "\n\n"

            else:

                chunks.append(current.strip())

                current = paragraph + "\n\n"

        if current:

            chunks.append(current.strip())

        return chunks
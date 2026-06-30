import re


class TextCleaner:
    """
    Text cleaner yang mengoptimalkan teks PDF untuk embedding.
    
    Menghilangkan:
    - Table of Contents markers (i, ii, iii, iv, romawi, dll)
    - Page numbers dan headers
    - Lines yang hanya dots/dashes
    - Newline berlebihan
    """

    def clean(self, text: str) -> str:
        """
        Clean teks dengan urutan operasi yang optimal.
        """
        # Step 1: Hapus page numbers (format: number di awal/akhir line)
        text = self._remove_page_numbers(text)

        # Step 2: Hapus TOC markers (romawi: i, ii, iii, iv, v, dst)
        text = self._remove_toc_markers(text)

        # Step 3: Hapus lines yang hanya decorative (dots, dashes)
        text = self._remove_decorative_lines(text)

        # Step 4: Hapus common PDF headers/footers
        text = self._remove_headers_footers(text)

        # Step 5: Normalize whitespace
        text = self._normalize_whitespace(text)

        # Step 6: Remove excessive newlines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Step 7: Strip awal/akhir
        text = text.strip()

        return text

    def _remove_page_numbers(self, text: str) -> str:
        """Hapus page numbers yang muncul di awal atau akhir baris."""
        # Pattern: line yang hanya berisi angka (1-999)
        text = re.sub(r"^\s*\d{1,3}\s*$", "", text, flags=re.MULTILINE)
        # Pattern: line yang hanya berisi angka di akhir dengan spasi
        text = re.sub(r"\n\s*\d{1,3}\s*\n", "\n", text)
        return text

    def _remove_toc_markers(self, text: str) -> str:
        """
        Hapus Table of Contents markers seperti:
        - Romawi kecil: i, ii, iii, iv, v, vi, vii, viii, ix, x
        - Patterns: "DAFTAR ISI", "Tabel", "Gambar", dll
        """
        # Hapus romawi markers di awal line (dengan atau tanpa spasi)
        text = re.sub(
            r"^\s*(?:i{1,3}|iv|v|vi{1,3}|ix|x)\s*$",
            "",
            text,
            flags=re.MULTILINE | re.IGNORECASE,
        )

        # Hapus common TOC headers
        toc_patterns = [
            r"^.*DAFTAR\s+ISI.*$",
            r"^.*TABEL\s+KONTEN.*$",
            r"^.*TABLE\s+OF\s+CONTENTS.*$",
            r"^.*LEMBAR\s+PERNYATAAN.*$",
            r"^.*KATA\s+PENGANTAR.*$",
            r"^.*ABSTRACT.*$",
            r"^.*ABSTRAK.*$",
        ]

        for pattern in toc_patterns:
            text = re.sub(pattern, "", text, flags=re.MULTILINE | re.IGNORECASE)

        return text

    def _remove_decorative_lines(self, text: str) -> str:
        """Hapus lines yang hanya berisi dots, dashes, atau decorative characters."""
        # Lines hanya dots (........)
        text = re.sub(r"^\s*\.{3,}\s*$", "", text, flags=re.MULTILINE)
        # Lines hanya dashes (-------)
        text = re.sub(r"^\s*-{3,}\s*$", "", text, flags=re.MULTILINE)
        # Lines hanya equals (=======)
        text = re.sub(r"^\s*={3,}\s*$", "", text, flags=re.MULTILINE)
        # Lines hanya underscores (_________)
        text = re.sub(r"^\s*_{3,}\s*$", "", text, flags=re.MULTILINE)
        # Lines dengan dots di tengah-tengah (ellipsis untuk TOC)
        text = re.sub(r".*\s+\.{4,}\s+\d+.*$", "", text, flags=re.MULTILINE)

        return text

    def _remove_headers_footers(self, text: str) -> str:
        """
        Hapus common PDF headers dan footers.
        Contoh: "Page 1 of 10", "Muhammad Hamzah - Thesis 2026"
        """
        # Pattern: "Page X of Y"
        text = re.sub(r"(?:page|halaman)\s+\d+\s+of\s+\d+", "", text, flags=re.IGNORECASE)

        # Pattern: "Page X" standalone
        text = re.sub(r"(?:page|halaman)\s+\d+$", "", text, flags=re.MULTILINE | re.IGNORECASE)

        # Pattern: names di footer (optional - bisa disesuaikan)
        text = re.sub(r"^Muhammad\s+Hamzah.*$", "", text, flags=re.MULTILINE)

        return text

    def _normalize_whitespace(self, text: str) -> str:
        """
        Normalize spasi:
        - Multiple spaces jadi single space
        - Multiple tabs jadi single space
        - Lines yang terputus karena PDF layout digabung
        """
        # Multiple spaces/tabs → single space
        text = re.sub(r"[ \t]+", " ", text)

        # Lines terputus di tengah kalimat (single newline → space)
        # Tapi preserve paragraphs (double newline)
        text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

        return text
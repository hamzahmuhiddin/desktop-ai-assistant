"""
Test script untuk Text Cleaner Upgrade
Pastikan semua noise dihapus dengan benar
"""

from src.rag.cleaner import TextCleaner

# Sample text dengan berbagai noise dari PDF
test_text = """
DAFTAR ISI
i
ii
iii
iv

LEMBAR PERNYATAAN.....................................................................1

Dengan ini menyatakan dengan sungguh-sungguh bahwa proposal penelitian saya

yang berjudul "Pertanggungjawaban Pidana Penyelenggara Sistem Elektronik Atas

Culpa Teknis Infrastruktur Jaringan Yang Mengakibatkan Kebocoran Data Pribadi"

Page 1 of 16

beserta seluruh isinya merupakan hasil karya saya sendiri.

Bogor, 20 Mei 2026

Muhammad Hamzah Muhiddin

KATA PENGANTAR
ii

Puji syukur senantiasa penulis panjatkan ke hadirat Allah SWT, karena atas
rahmat dan karunia-Nya, penulis dapat menyelesaikan proposal tesis ini.

---

ABSTRAK
iii

Penelitian ini bertujuan mengkaji pertanggungjawaban pidana Penyelenggara Sistem
Elektronik (PSE) atas culpa teknis dalam pemeliharaan infrastruktur jaringan.

Page 2 of 16

Insiden Pusat Data Nasional Sementara 2 (PDNS 2) pada Juni 2024 menunjukkan bahwa
penegakan hukum atas penyelenggara sistem elektronik masih memerlukan landasan doktrin
yang lebih kokoh.

Penelitian ini menggunakan pendekatan kualitatif dengan jenis penelitian
yuridis-normatif.

===================================================

BAB I PENDAHULUAN

A. Latar Belakang

Indonesia menempati peringkat ketiga negara di kawasan ASEAN dengan jumlah
insiden kebocoran data terbanyak, suatu kondisi yang mengindikasikan bahwa pertumbuhan
infrastruktur digital nasional belum disertai penerapan standar keamanan yang proporsional.
"""

print("=" * 70)
print("TEST: Text Cleaner Upgrade")
print("=" * 70)

cleaner = TextCleaner()
cleaned = cleaner.clean(test_text)

print("\n📊 HASIL CLEANING:\n")
print(cleaned)

print("\n" + "=" * 70)
print("✓ CHECKS:\n")

checks = [
    ("❌ DAFTAR ISI dihapus", "DAFTAR ISI" not in cleaned),
    ("❌ Romawi (i, ii, iii) dihapus", "^i$" not in cleaned and "^ii$" not in cleaned),
    ("❌ Page numbers dihapus", "Page 1 of 16" not in cleaned),
    ("❌ Decorative lines dihapus", "===" not in cleaned),
    ("❌ KATA PENGANTAR dihapus", "KATA PENGANTAR" not in cleaned),
    ("✅ Content preserved", "Penelitian ini bertujuan" in cleaned),
    ("✅ Paragraphs maintained", "\n\n" in cleaned),
]

for check_name, result in checks:
    status = "✓" if result else "✗"
    print(f"{status} {check_name}")

print("\n" + "=" * 70)
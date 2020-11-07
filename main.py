# DDP LAB-4
# Nama: <Tulis nama di sini>
# NIM: <Tulis NIM di sini>

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini
nama = input("Masukkan nama: ")
lenNama = len(nama)
iNama = 1
while iNama <= lenNama:
  print(nama[0:iNama])
  iNama = iNama + 1



# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini
text = input("\nMasukkan text: ")

if len(text) >= 8 and ( 'nf' in text.lower()) and (text.endswith('YYY') or text.endswith('yyy')) and any(char.isdigit() for char in text):
  print("Teks valid. Program berhenti.")
else:
  print("Teks tidak valid.")
  
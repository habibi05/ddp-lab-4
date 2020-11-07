# DDP LAB-4
# Nama: Habibi
# NIM: 0110220247

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini

# Simpan masukan nama kedalam variabel nama
nama = input("Masukkan nama: ")
# Simpan panjang nama kedalam variabel lenNama
lenNama = len(nama)
# Deklarasi variabel iNama dengan nilai 1 untuk kebutuhan perulangan
iNama = 1
# Lakukan perulangan sebanyak nilai yang ada di variabel lenNama
while iNama <= lenNama:
  # print nama dengan String Slicing sesuai urutan perulangan
  print(nama[0:iNama])
  # tambahkan nilai iNama dengan 1
  iNama = iNama + 1


# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini

# Simpan masukan text kedalam variabel text
text = input("\nMasukkan text: ")

# Program melakukan pengecekan apakah panjang text lebih atau sama dengan 8, terdapat kata nf, terdapat YYY atau yyy, dan terdapat angka di dalam text tersebut
if len(text) >= 8 and ( 'nf' in text.lower()) and (text.endswith('YYY') or text.endswith('yyy')) and any(char.isdigit() for char in text):
  # jika memenuhi syarat maka print
  print("Teks valid. Program berhenti.")
else:
  # jika tidak memenuhi syarat maka print
  print("Teks tidak valid.")
  
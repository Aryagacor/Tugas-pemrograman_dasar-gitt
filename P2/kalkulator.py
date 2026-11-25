
# Program Kalkulator Sederhana

# Input
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Proses
tambah = angka1 + angka2
kurang = angka1 - angka2
kali = angka1 * angka2

# Output
print("\n===== HASIL KALKULATOR =====")
print(f"Penjumlahan : {tambah}")
print(f"Pengurangan : {kurang}")
print(f"Perkalian   : {kali}")

if angka2 != 0:
    bagi = angka1 / angka2
    print(f"Pembagian   : {bagi}")
else:
    print("Pembagian   : Tidak bisa dibagi nol")
  

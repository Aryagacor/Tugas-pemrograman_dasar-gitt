
# Program Kasir Sederhana

# Input
nama_barang = input("Masukkan nama barang: ")
harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))

# Proses
total = harga * jumlah

# Output
print("\n===== STRUK BELANJA =====")
print(f"Nama barang : {nama_barang}")
print(f"Harga       : Rp{harga}")
print(f"Jumlah      : {jumlah}")
print(f"Total       : Rp{total}")

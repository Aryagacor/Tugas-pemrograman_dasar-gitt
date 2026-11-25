
# Program Menghitung Diskon

# Input
harga = int(input("Masukkan harga barang: "))
diskon = float(input("Masukkan diskon (%): "))

# Proses
potongan = harga * diskon / 100
total_bayar = harga - potongan

# Output
print("\n===== HASIL PERHITUNGAN =====")
print(f"Harga awal    : Rp{harga}")
print(f"Diskon        : {diskon}%")
print(f"Potongan      : Rp{potongan:.0f}")
print(f"Total bayar   : Rp{total_bayar:.0f}")

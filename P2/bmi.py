
# Program Menghitung BMI

# Input
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter): "))

# Proses
bmi = berat / (tinggi ** 2)

# Output
print(f"Nilai BMI kamu adalah: {bmi:.2f}")

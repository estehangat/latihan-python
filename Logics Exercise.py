# Latihan logika menggunakan Comparison

angka = float(input("Angka kurang dari 9 atau lebih dari 21 : "))

# Lebih dari sama dengan
lebih = (angka >= 21)
print("Angka anda lebih dari 21", lebih)

# Kurang dari sama dengan
kurang = (angka <= 9)
print("Angka anda kurang dari 9", kurang)

# Irisan
correct = lebih and kurang
print("Angka anda beririsan", correct)
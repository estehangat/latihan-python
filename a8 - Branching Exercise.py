# Latihan Percabangan

print(10*"=", "Kalkulator Sederhana", "="*10)
angka1 = float(input("Ketik suatu angka \t: ")) # Input : 21
operator = input("Pilih suatu operator \n1. +\n2. -\n3. x\n4. :\n")
angka2 = float(input("Ketik angka lagi \t: ")) # Input : 9

if operator == "1":
    hasil = angka1 + angka2
    print(f"Hasil \t: {hasil:.2f}") # Output : Hasil : 30.00
elif operator == "2":
    hasil = angka1 - angka2
    print(f"Hasil \t: {hasil:.2f}") # Output : Hasil : 12.00
elif operator == "3":
    hasil = angka1 * angka2
    print(f"Hasil \t: {hasil:.2f}") # Output : Hasil : 189.00
elif operator == "4":
    hasil = angka1 / angka2
    print(f"Hasil \t: {hasil:.2f}") # Output : Hasil : 2.33
else :
    print("Operator yang anda masukkan salah, Silakan ulangi") # Output : Operator yang anda masukkan salah, Silakan ulangi 
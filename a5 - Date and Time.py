# Date and time

'''
    For more information, visit
    https://www.w3schools.com/python/python_datetime.asp
'''

import datetime

# Tanggal Hari Ini
harini = datetime.date.today()
print(harini) # Output : 2023-07-05

# Tanggal Random
tanggal = datetime.date(2005,5,21)
print(tanggal) # Output : 2005-05-21

# Input Tanggal
hari = int(input("Hari \t: ")) # Input : 9
bulan = int(input("Bulan \t: ")) # Input : 1
tahun = int(input("Tahun \t: ")) # Input : 2006
hasil = datetime.date(tahun,bulan,hari)
print(hasil) # Output : 2006-01-09
print(f"Itu adalah hari {hasil:%A}") # Output : Itu adalah hari Monday

# Menghitung Umur
umur = harini - hasil
umurFix = umur.days // 365
umurSisa = (umur.days % 365) // 30
print(f"Umur Input adalah : {umurFix} tahun, {umurSisa} bulan") # Umur Input adalah : 17 tahun
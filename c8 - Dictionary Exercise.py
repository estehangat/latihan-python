import datetime
import os

# Template Mahasiswa
template = {
    'Nama':'Nama',
    'NIM':000000000,
    'Lahir':datetime.datetime(1111,1,11),
    'SKS':0
}

data = {}
os.system("cls") # Untuk Windows, Untuk Menghilangkan Tulisan Path System

print(f"{'ARSIP DATA':^16}\n {'MAHASISWA':^16}")
print("="*16)

mahasiswa = dict.fromkeys(template.keys())
print(mahasiswa) # Output : {'Nama': None, 'NIM': None, 'Lahir': None, 'SKS': None}
mahasiswa['Nama'] = input("Nama \t\t: ")
mahasiswa['NIM'] = input("NIM \t\t: ")
TAHUN = int(input("Tahun (yyyy) \t: "))
BULAN = int(input("Bulan (mm) \t: "))
TANGGAL = int(input("Tanggal (dd) \t: "))
mahasiswa['Lahir'] = datetime.datetime(TAHUN,BULAN,TANGGAL)
mahasiswa['SKS'] = input("SKS \t\t: ")
print(mahasiswa) # Output : {'Nama': None, 'NIM': None, 'Lahir': None, 'SKS': None}
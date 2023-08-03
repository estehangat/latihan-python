import datetime
import os
import string
import random

# Template Mahasiswa
template = {
    'Nama':'Nama',
    'NIM':000000000,
    'Lahir':datetime.datetime(1111,1,11),
    'SKS':0
}

data = {}

while True:
    os.system("cls") # Untuk Windows, Untuk Menghilangkan Tulisan Path System

    print(f"{'ARSIP DATA':^16}\n {'MAHASISWA':^16}")
    print("="*16)

    mahasiswa = dict.fromkeys(template.keys())
    mahasiswa['Nama'] = input("Nama \t\t: ")
    mahasiswa['NIM'] = input("NIM \t\t: ")
    TAHUN = int(input("Tahun (yyyy) \t: "))
    BULAN = int(input("Bulan (mm) \t: "))
    TANGGAL = int(input("Tanggal (dd) \t: "))
    mahasiswa['Lahir'] = datetime.datetime(TAHUN,BULAN,TANGGAL)
    mahasiswa['SKS'] = input("SKS \t\t: ")

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
    data.update({KEY:mahasiswa})

    print('\n')
    print(f"| {'KEY':^6} | {'NAMA':^18} | {'NIM':^12} | {'LAHIR':^10} | {'SKS':^8} |")
    print("="*70)

    for key in data:
        KEY = key
        NAMA = data[KEY]['Nama']
        NIM = data[KEY]['NIM']
        LAHIR = data[KEY]['Lahir'].strftime("%x")
        SKS = data[KEY]['SKS']
        print(f"| {KEY:<6} | {NAMA:<18} | {NIM:<12} | {LAHIR:<10} | {SKS:<8} |")

    print('\n')

    done = input("Apakah sudah selesai? (y/n) ") # Output : Apakah sudah selesai? (y/n)
    if done == 'y':
        break

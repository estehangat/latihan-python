# Operasi Dictionary

data = {
    'a':'Halland',
    'b':'Kovacic',
    'c':'Foden',
    'd':'De Bruyne'
}

# Panjang Dictionary
LONG = len(data)
print(f"Panjang Data adalah {LONG}") # Output : Panjang Data adalah 4

# Mengecek Key Exist atau Tidak
KEY = 'c'
CHECK = KEY in data
print(f"Apakah data 'c' ada di dalam data? {CHECK}") # Output : Apakah data 'c' ada di dalam data? True

# Mengakses Value (read) dengan Get
print(data['a']) # Output : Halland
print(data.get('d')) # Output : De Bruyne
print(data.get('e','Key tidak ditemukan')) # Cek key dengan message

# Mengupdate Data
data['b'] = 'Ruben'
print(f"Data 'b' telah diupdate menjadi {data['b']}") # Output : Data 'b' telah diupdate menjadi Ruben

# Menambah Data
data['e'] = 'Ederson'
print(f"Data baru 'e' telah ditambahkan yaitu {data['e']}") # Output : Data baru 'e' telah ditambahkan yaitu Ederson

data.update({'f':'Alvarez'})
print(f"Data terupdate setelah ditambah 'f' adalah {data}") # Output : Data terupdate setelah ditambah 'f' adalah {'a': 'Halland', 'b': 'Ruben', 'c': 'Foden', 'd': 'De Bruyne', 'e': 'Ederson', 'f': 'Alvarez'}

# Menghapus Data pada Dictionary
del data['b']
print(f"Data terupdate setelah 'b' dihapus adalah {data}") # Output : {'a': 'Halland', 'c': 'Foden', 'd': 'De Bruyne', 'e': 'Ederson', 'f': 'Alvarez'}
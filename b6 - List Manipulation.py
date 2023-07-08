## List

# Index
data = ["Bill","Gates","Elon","Musk"]

# Mengambil Data dari List
userData = data[0] # 0 = Pertama
print(f"Data Terambil {userData}") # Output : Data Terambil Bill

userData = data[-1] # -1 = Terakhir
print(f"Data Terambil {userData}") # Output : Data Terambil Musk

# Mengambil Jumlah Data dari List
userData = len(data)
print(f"Data Sebanyak {userData}") # Output : Data Sebanyak 4

## Manipulasi Data

# Menambahkan Data Pada List
data.insert(2,"Zuck")
print(f"Data Terbaru {data}") # Output : Data Terbaru ['Bill', 'Gates', 'Zuck', 'Elon', 'Musk']

# Menambah Data di Akhir List
data.append("MrBeast")
print(f"Newest Data {data}") # Output : Newest Data ['Bill', 'Gates', 'Zuck', 'Elon', 'Musk', 'MrBeast']

# Menggabungkan Data Baru
dataNew = ["Jeff","Bezos"]
data.extend(dataNew)
print(f"The Great Data {data}") # Output : The Great Data ['Bill', 'Gates', 'Zuck', 'Elon', 'Musk', 'MrBeast', 'Jeff', 'Bezos']

# Mengubah Suatu Data dari List
data[2] = "Jabieb"
print(f"Great Super Data {data}") # Output : Great Super Data ['Bill', 'Gates', 'Jabieb', 'Elon', 'Musk', 'MrBeast', 'Jeff', 'Bezos']

# Menghapus Suatu Data dari List
data.remove("MrBeast")
print(f"Master Data {data}") # Output : Master Data ['Bill', 'Gates', 'Jabieb', 'Elon', 'Musk', 'Jeff', 'Bezos']

# Menghapus Data Paling Akhir
dataIlang = data.pop() # Hanya data.pop()
print(f"Data Akhir {data}") # Output : Data Akhir ['Bill', 'Gates', 'Jabieb', 'Elon', 'Musk', 'Jeff']
print(dataIlang) # Output : Bezos
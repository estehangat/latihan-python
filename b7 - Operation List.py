# Operasi List

# Count Data
dataNumber = [1,6,4,4,4,2,6,8,9,0,6,2,9,0,6,1,2,8]
data6 = dataNumber.count(6)
print(f"Angka 6 Muncul {data6} kali") # Output : Angka 6 Muncul 4 kali

# Index
data = ["Bill","Gates","Elon","Musk"]
dataIndex = data.index("Elon")
print(f"{data[2]} Ada di data ke-{dataIndex}") # Output : Elon Ada di data ke-2

# Mengurutkan List
dataNumber.sort()
print(dataNumber) # Output : [0, 0, 1, 1, 2, 2, 2, 4, 4, 4, 6, 6, 6, 6, 8, 8, 9, 9]

data.sort()
print(data) # Output : ['Bill', 'Elon', 'Gates', 'Musk']

# Membalik Data
dataNumber.reverse()
data.reverse()
print(dataNumber) # Output : [9, 9, 8, 8, 6, 6, 6, 6, 4, 4, 4, 2, 2, 2, 1, 1, 0, 0]
print(data) # Output : ['Musk', 'Gates', 'Elon', 'Bill']

# Copy List
data = ["Windah","Basudara","Tukul"]
dataCopy = data.copy()
dataCopy[1] = "Bersaudara"
print(data) # Output : ['Windah', 'Basudara', 'Tukul']
print(dataCopy) # Output : ['Windah', 'Bersaudara', 'Tukul']

# Menyambung String (Concatenate)

awal = "Monkey"
tengah = "D"
akhir = "Luffy"
lengkap = awal + " " + tengah + "'" + akhir
print(lengkap)

# Menghitung Panjang String
long = len(lengkap)
print(long)

# Mengecek Komponen String
p = "p"
stats = p in lengkap
print(stats)

p = "p"
stats = p not in lengkap
print(stats)

# Mengulang String
print("W"*9)
print(9*"W")

# Indexing
print("Huruf ke-1", lengkap[0])
print("Huruf ke-9", lengkap[10])
print("Huruf ke-7-9", lengkap[6:8])
print("Huruf ke-2,4,6,8,10", lengkap[1:9:2])

# Ascii Code
min = min(lengkap)
max = max(lengkap)
min1 = ord(min)
max1 = ord(max)
print("Ascii Code paling kecilnya yaitu", min, "dengan angka", min1)
print("Ascii Code paling besarnya yaitu", max, "dengan angka", max1)

# Counting
full = lengkap.count('y')
print("Jumlah huruf y pada", "'" + lengkap + "'", "adalah", full)

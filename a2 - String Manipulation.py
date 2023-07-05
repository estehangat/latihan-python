# Menyambung String (Concatenate)

awal = "Monkey"
tengah = "D"
akhir = "Luffy"
lengkap = awal + " " + tengah + "'" + akhir
print(lengkap) # Output : Monkey D'Luffy

# Menghitung Panjang String
long = len(lengkap)
print(long) # Output : 14

# Mengecek Komponen String
p = "p"
stats = p in lengkap
print(stats) # Output : False

p = "p"
stats = p not in lengkap
print(stats) # Output : True

# Mengulang String
print("W"*9) # Output : WWWWWWWWW
print(9*"W") # Output : WWWWWWWWW

# Indexing
print("Huruf ke-1", lengkap[0]) # Output : Huruf ke-1 M
print("Huruf ke-9", lengkap[10]) # Output : Huruf ke-9 u
print("Huruf ke-7-9", lengkap[6:8]) # Output : Huruf ke-7-9  D
print("Huruf ke-2,4,6,8,10", lengkap[1:9:2]) # Output : Huruf ke-2,4,6,8,10 okyD

# Ascii Code
min = min(lengkap)
max = max(lengkap)
min1 = ord(min)
max1 = ord(max)
print("Ascii Code paling kecilnya yaitu", min, "dengan angka", min1) # Output : Ascii Code paling kecilnya yaitu   dengan angka 32
print("Ascii Code paling besarnya yaitu", max, "dengan angka", max1) # Output : Ascii Code paling besarnya yaitu y dengan angka 121

# Counting
full = lengkap.count('y')
print("Jumlah huruf y pada", "'" + lengkap + "'", "adalah", full) # Output : Jumlah huruf y pada 'Monkey D'Luffy' adalah 2

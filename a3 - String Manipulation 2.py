'''
    For more information, visit
    https://www.w3schools.com/python/python_strings_methods.asp
'''

# Upper
upper = "Hello".upper()
print(upper)

## Mengecek Upper
aa = "MICROSOFT"
up = aa.isupper()
print(up)

# Lower
lower = "Hello".lower()
print(lower)

## Mengecek Lower
bb = "microsoft"
low = bb.islower()
print(low)

# Capitalize
capt = "hello".capitalize()
print(capt)

# isalpha() -> semua huruf
# isalnum() -> huruf dan angka
# isdecimal() -> semua angka
# isspace() -> spasi, tab, newline
# istitle() -> semua kata diawali huruf besar

# Starts With
starts = "Bill Gates".startswith("Bill")
print(starts)

# Ends With
ends = "Bill Gates".endswith("Gates")
print(ends)

# Penggabungan Komponen
## Join
join = ['Elon','Musk','SpaceX']
gabung = ','.join(join)
print(gabung)

## Split
split = "ElonwMuskwSpaceX"
print(split.split("w"))

# Alokasi Karakter
## Ke Kanan
kanan = "Microsoft".rjust(10)
print("'" + kanan + "'")

## Ke Kiri
kiri = "Microsoft".ljust(10)
print("'" + kiri + "'")

## Ke Tengah
tengah = "Microsoft".center(11,"W")
print("'" + tengah + "'")

# Menghilangkan Tanda dari Alokasi
strip = tengah.strip("W")
print("'" + strip + "'")
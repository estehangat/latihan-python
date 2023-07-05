'''
    For more information, visit
    https://www.w3schools.com/python/python_strings_methods.asp
'''

# Upper
upper = "Hello".upper()
print(upper) # Output : HELLO

## Mengecek Upper
aa = "MICROSOFT"
up = aa.isupper()
print(up) # Output : True

# Lower
lower = "Hello".lower()
print(lower) # Output : hello

## Mengecek Lower
bb = "microsoft"
low = bb.islower()
print(low) # Output : True

# Capitalize
capt = "hello".capitalize()
print(capt) # Output : Hello

# isalpha() -> semua huruf
# isalnum() -> huruf dan angka
# isdecimal() -> semua angka
# isspace() -> spasi, tab, newline
# istitle() -> semua kata diawali huruf besar

# Starts With
starts = "Bill Gates".startswith("Bill")
print(starts) # Output : True

# Ends With
ends = "Bill Gates".endswith("Gates")
print(ends) # Output : True

# Penggabungan Komponen
## Join
join = ['Elon','Musk','SpaceX']
gabung = ','.join(join)
print(gabung) # Output : Elon,Musk,SpaceX

## Split
split = "ElonwMuskwSpaceX"
print(split.split("w")) # Output : ['Elon', 'Musk', 'SpaceX']

# Alokasi Karakter
## Ke Kanan
kanan = "Microsoft".rjust(10)
print("'" + kanan + "'") # Output : ' Microsoft'

## Ke Kiri
kiri = "Microsoft".ljust(10)
print("'" + kiri + "'") # Output : 'Microsoft '

## Ke Tengah
tengah = "Microsoft".center(11,"W")
print("'" + tengah + "'") # Output : 'WMicrosoftW'

# Menghilangkan Tanda dari Alokasi
strip = tengah.strip("W")
print("'" + strip + "'") # Output : 'Microsoft'

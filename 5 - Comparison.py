# Operasi Komparasi
# Setiap hasil dari komparasi adalah boolean
# >, <, >=, <=, ==, !=, is, is not

a = 21
b = 9

# Lebih besar (>)
c = a > b
print(a, '>', b, c)

# Lebih kecil (<)
c = a < b
print(a, '<', b, c)

# Lebih besar sama dengan (>=)
c = a >= b
print(a, '>=', b, c)

# Lebih kecil sama dengan (<=)
c = a <= b
print(a, '<=', b, c)

# Sama dengan (==)
c = a == b
print(a, '==', b, c)

# Tidak sama dengan (!=)
c = a != b
print(a, '!=', b, c)

## Komparasi Object Identity

# is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
p = x is ["apple", "banana"]
print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content (True jika object adalah angka)
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print(p) # True jika object adalah angka

# is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
p = x is not ["apple", "banana"]
print(x is not z) # returns True because z is the same object as x
print(x is not y) # returns False because x is not the same object as y, even if they have the same content (True jika object adalah angka)
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print(p) # True jika object adalah angka

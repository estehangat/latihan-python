# Operasi Komparasi
# Setiap hasil dari komparasi adalah boolean
# >, <, >=, <=, ==, !=, is, is not

a = 21
b = 9

# Lebih besar (>)
c = a > b
print(a, '>', b, c) # Output : 21 > 9 True

# Lebih kecil (<)
c = a < b
print(a, '<', b, c) # Output : 21 < 9 False

# Lebih besar sama dengan (>=)
c = a >= b
print(a, '>=', b, c) # Output : 21 >= 9 True

# Lebih kecil sama dengan (<=)
c = a <= b
print(a, '<=', b, c) # Output : 21 <= 9 False

# Sama dengan (==)
c = a == b
print(a, '==', b, c) # Output : 21 == 9 False

# Tidak sama dengan (!=)
c = a != b
print(a, '!=', b, c) # Output : 21 != 9 True

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

# Output :
# True
# False
# True
# False

# is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
p = x is not ["apple", "banana"]
print(x is not z) # returns True because z is the same object as x
print(x is not y) # returns False because x is not the same object as y, even if they have the same content (True jika object adalah angka)
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print(p) # True jika object adalah angka

# Output :
# False
# True
# True
# True

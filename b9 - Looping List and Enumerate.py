# Looping List

# For Loop dan Range
angka = [1,6,8,9,3,6,2]
long = len(angka)

for i in range(long):
    print(f"Angka {angka[i]}") # Output : Angka 1,6,8,9,3,6,2

print("")

# While
angka = [1,6,8,9,3,6,2]
long = len(angka)
i = 0

while i < long:
    print(f"Angka {angka[i]}") # Output : Angka 1,6,8,9,3,6,2
    i += 1

print("")

# List Comprehension
i = 1
i += 1
list = [7,21,"Maeng"]

[print(f"List {i}") for i in list] # Output : List 7,21,Maeng

# Enumerate
list = [7,21,"Maeng"]

for i, p in enumerate(list):
    print(f"Index {i}, List {p}") # Output : Index 0,1,2 List 7,21,Maeng
# Latihan Perulangan

user = 21
## For
count = 1
for i in range(9):
    print("$"*count) # Output : $
    count += 1

print("\n")

## While
count = 1
while True:
    print("$"*count) # Output : $
    count += 1
    if count > user:
        break

## Continue
user = 10
count = 1
while True:
    if (count%2):
    # Print jika ganjil
        print("$"*count) # Output : $
        count += 1
    else: 
    # Kembali ke atas jika ganjil
        count += 1
        continue
    if count > user:
    # Break jika count melebihi user
        break

## Segitiga Sama Kaki
user = 10
count = 1
space = int(user/2)
while True:
    if (count%2):
    # Print jika ganjil
        print(" "*space, "+"*count) # Output : +
        space -= 1
        count += 1
    else: 
    # Kembali ke atas jika ganjil
        count += 1
        continue
    if count > user:
    # Break jika count melebihi user
        break

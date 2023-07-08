# List

# List Angka
list = [0,1,2,3,4,5,6,7,8,9]
print(list) # Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List String
list = ["Bill","Gates","Elon"]
print(list) # Output : ['Bill', 'Gates', 'Elon']

# List Boolean
list = [True,False,True]
print(list) # Output : [True, False, True]

# List Campur
list = [0,"Musk",2,3,"Zuck"]
print(list) # Output : [0, 'Musk', 2, 3, 'Zuck']

# Menggunakan For Loop
list = [i**2 for i in range(0,10+1,2)]
print(list) # Output : [0, 4, 16, 36, 64, 100]

# Menggunakan If
list = [i for i in range(0,10) if i != 9]
print(list) # Output : [0, 1, 2, 3, 4, 5, 6, 7, 8]

list = [i for i in range(0,10) if i%2 == 0]
print(list) # Output : [0, 2, 4, 6, 8]
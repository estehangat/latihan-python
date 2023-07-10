# Nested List

dataNormal = [1001,1002,2005,2006]
data0 = [1001,1002]
data1 = [2005,2006]
dataList = [data0,data1,21,9]

print(dataNormal) # Output : [1001, 1002, 2005, 2006]
print(dataList) # Output : [[1001, 1002], [2005, 2006], 21, 9]

# Contoh Penggunaan
user1 = ["Windah",30,"Male"]
user2 = ["Tukul",27,"Male"]
user3 = ["Ella",16,"Female"]
userNew = [user1,user2,user3]

for name in userNew:
    print(f"Name\t: {name[0]}") # Output : Name : Windah, Tukul, Ella
    print(f"Age\t: {name[1]}") # Output : Age : 30, 27, 16
    print(f"Gender\t: {name[2]}") # Output : Gender : Male, Male, Female
    print(16*"=") # Output : ================
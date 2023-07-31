# Program List Pemain

userList = []
while True:
    print("Insert Nama Pemain dan Klub")
    pemain = input("Nama Pemain \t: ")
    klub = input("Nama Klub \t: ")

    list = [pemain,klub]
    userList.append(list)

    print("\n"+"="*10)
    for i,j in enumerate(userList):
        print(f"{i+1} - {j[0]} - {j[1]}")

    print("\n"+"="*10)
    cont = input("Continue? (y/n)")

    if cont == "n":
        break
# Continue
user = 0
while user < 7:
    user += 1
    print(f"Just my homie {user}") # Output : Just my homie 1-7

    if user == 3:
        print("That's my G") # Output : That's my G
        continue # Membuat loop loncat ke step selanjutnya
    print("TF G") # Output : TF G

# Pass
user = 0
while user < 9:
    user += 1
    if user == 7:
        pass # Ini hanya dummy
    print(user) # Output : 1-9
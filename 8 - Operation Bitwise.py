# Operator Bitwise

a = 21
b = 9
print("Angka", a, "binernya yaitu", format(a,"08b")) # Output : Angka 21 binernya yaitu 00010101
print("Angka", b, "binernya yaitu", format(b,"08b")) # Output : Angka 9 binernya yaitu 00001001
print("\n")

# OR (|)
c = a | b
print(5*"*"+"OR"+5*"*") # Output : *****OR*****
print("Angka", c, "binernya yaitu", format(c,"08b")) # Output : Angka 29 binernya yaitu 00011101
print("\n")

# AND (&)
c = a & b
print(5*"*"+"AND"+5*"*") # Output : *****AND*****
print("Angka", c, "binernya yaitu", format(c,"08b")) # Output : Angka 1 binernya yaitu 00000001
print("\n")

# XOR (^)
c = a ^ b
print(5*"*"+"XOR"+5*"*") # Output : *****XOR*****
print("Angka", c, "binernya yaitu", format(c,"08b")) # Output : Angka 28 binernya yaitu 00011100
print("\n")

# Shifting
print(5*"*"+"SHIFTING"+5*"*") # Output : *****SHIFTING*****
c = a >> 2
print("Angka", c, "binernya yaitu", format(c,"08b")) # Output : Angka 5 binernya yaitu 00000101
c = a << 2
print("Angka", c, "binernya yaitu", format(c,"08b")) # Output : Angka 84 binernya yaitu 01010100

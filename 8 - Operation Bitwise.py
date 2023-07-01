# Operator Bitwise

a = 21
b = 9
print("Angka", a, "binernya yaitu", format(a,"08b"))
print("Angka", b, "binernya yaitu", format(b,"08b"))
print("\n")

# OR (|)
c = a | b
print(5*"*"+"OR"+5*"*")
print("Angka", c, "binernya yaitu", format(c,"08b"))
print("\n")

# AND (&)
c = a & b
print(5*"*"+"AND"+5*"*")
print("Angka", c, "binernya yaitu", format(c,"08b"))
print("\n")

# XOR (^)
c = a ^ b
print(5*"*"+"XOR"+5*"*")
print("Angka", c, "binernya yaitu", format(c,"08b"))
print("\n")

# Shifting
print(5*"*"+"SHIFTING"+5*"*")
c = a >> 2
print("Angka", c, "binernya yaitu", format(c,"08b"))
c = a << 2
print("Angka", c, "binernya yaitu", format(c,"08b"))
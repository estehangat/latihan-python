# Contoh Generic
## String
user = "Deadlock"
string = f"Hello {user}!"
print(string) # Output : Hello Deadlock!

## Number
user = 90106
string = f"Angka {user}"
print(string) # Output : Angka 90106

## Boolean
user = True
string = f"Apakah {user}?"
print(string) # Output : Apakah True?

## Bilangan Bulat
user = 21
string = f"Bulat {user:d}"
print(string) # Output : Bulat 21

## Bilangan Ribuan
user = 21900
string = f"Ribuan {user:,}"
print(string) # Output : Ribuan 21,900

## Bilangan Desimal
user = 215.901
string = f"Desimal {user:.1f}"
print(string) # Output : Desimal 215.9

## Leading Zero
user = 215.901
string = f"Leading Zero {user:010.1f}"
print(string) # Output : Leading Zero 00000215.9

## Plus Minus
plus = +21
minus = -9
string1 = f"Plus {plus:+d}"
string2 = f"Minus {minus}" # Minus selalu terlihat meskipun tidak :+d
print(string1) # Output : Plus +21
print(string2) # Output : Minus -9

## Persen
user = 0.219
string = f"Persen {user:.1%}"
print(string) # Output : Persen 21.9%

# Format Angka Lain (binary, octal, hexadecimal)
angka = 219
binary = f"Binary {bin(angka)}"
octal = f"Octal {oct(angka)}"
hex = f"Hexadecimal {hex(angka)}"
print(binary) # Output : Binary 0b11011011
print(octal) # Output : Octal 0o333
print(hex) # Output : Hexadecimal 0xdb

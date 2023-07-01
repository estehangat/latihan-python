# and, or, xor, not
# &    |    ^    ~

# AND (ada False maka False) (&)
a = True
b = False
c = a and b
print("*****AND*****")
print(a, 'and', b, 'adalah', c)

a = True
b = True
c = a and b
print(a, 'and', b, 'adalah', c)

a = False
b = False
c = a and b
print(a, 'and', b, 'adalah', c)
print('\n')

# OR (ada True maka True) (|)
print("*****OR*****")
a = True
b = False
c = a or b
print(a, 'or', b, 'adalah', c)

a = True
b = True
c = a or b
print(a, 'or', b, 'adalah', c)

a = False
b = False
c = a or b
print(a, 'or', b, 'adalah', c)
print('\n')

# XOR (jika sama maka False, beda maka True) (^)
print("*****XOR*****")
a = True
b = False
c = a ^ b
print(a, 'xor', b, 'adalah', c)

a = True
b = True
c = a ^ b
print(a, 'xor', b, 'adalah', c)

a = False
b = False
c = a ^ b
print(a, 'xor', b, 'adalah', c)
print('\n')

# NOT (~)
print("*****NOT*****")
a = True
c = not a
print(a, 'not', c)

a = False
c = not a
print(a, 'not', c)
print('\n')

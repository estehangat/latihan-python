# and, or, xor, not
# &    |    ^    ~

# AND (ada False maka False) (&)
a = True
b = False
c = a and b
print("*****AND*****") # Output : *****AND*****
print(a, 'and', b, 'adalah', c) # Output : True and False adalah False

a = True
b = True
c = a and b
print(a, 'and', b, 'adalah', c) # Output : True and True adalah True

a = False
b = False
c = a and b
print(a, 'and', b, 'adalah', c) # Output : False and False adalah False
print('\n')

# OR (ada True maka True) (|)
print("*****OR*****") # Output : *****OR*****
a = True
b = False
c = a or b
print(a, 'or', b, 'adalah', c) # Output : True or False adalah True

a = True
b = True
c = a or b
print(a, 'or', b, 'adalah', c) # Output : True or True adalah True

a = False
b = False
c = a or b
print(a, 'or', b, 'adalah', c) # Output : False or False adalah False
print('\n')

# XOR (jika sama maka False, beda maka True) (^)
print("*****XOR*****") # Output : *****XOR*****
a = True
b = False
c = a ^ b
print(a, 'xor', b, 'adalah', c) # Output : True xor False adalah True

a = True
b = True
c = a ^ b
print(a, 'xor', b, 'adalah', c) # Output : True xor True adalah False

a = False
b = False
c = a ^ b
print(a, 'xor', b, 'adalah', c) # Output : False xor False adalah False
print('\n')

# NOT (~)
print("*****NOT*****") # Output : *****NOT*****
a = True
c = not a
print(a, 'not', c) # Output : True not False

a = False
c = not a
print(a, 'not', c) # Output : False not True
print('\n')

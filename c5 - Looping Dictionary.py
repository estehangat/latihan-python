# Looping Dictionary

guns = {
    'key1':'Vandal',
    'key2':'Phantom',
    'key3':'Operator',
    'key4':'Judge'
}

# Looping First Try (Outputnya Key)
for key in guns:
    print(key) # Output : key1, key2, key3, key4

# Operator untuk mengambil item / iterables
keys = guns.keys()
print(keys) # Output : dict_keys(['key1', 'key2', 'key3', 'key4'])

for key in guns:
    print(guns.get(key)) # Output : Vandal, Phantom, Operator, Judge

value = guns.values()
print(value) # Output : dict_values(['Vandal', 'Phantom', 'Operator', 'Judge'])

for nilai in value:
    print(nilai) # Output : Vandal, Phantom, Operator, Judge

item = guns.items()
print(item) # Output : dict_items([('key1', 'Vandal'), ('key2', 'Phantom'), ('key3', 'Operator'), ('key4', 'Judge')])

for item in item:
    print(item) # Output : ('key1', 'Vandal'), ('key2', 'Phantom'), ('key3', 'Operator'), ('key4', 'Judge')

for key,value in guns.items():
    print(f"Key \t: {key} | Value \t: {value}") # Output : Key     : key1 | Value  : Vandal, Key     : key2 | Value  : Phantom, Key     : key3 | Value  : Operator, Key     : key4 | Value  : Judge
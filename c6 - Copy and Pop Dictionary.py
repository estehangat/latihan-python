# Copy Dictionary

data = {
    'a':'Halland',
    'b':'Kovacic',
    'c':'Foden',
    'd':'De Bruyne'
}

dataCopy = data.copy()
data['a'] = 'Alvarez'
print(f"Ini adalah Data \t: {data}") # Output : Ini adalah Data : {'a': 'Alvarez', 'b': 'Kovacic', 'c': 'Foden', 'd': 'De Bruyne'}
print(f"Ini adalah Data Copy \t: {dataCopy}") # Output : Ini adalah Data Copy : {'a': 'Halland', 'b': 'Kovacic', 'c': 'Foden', 'd': 'De Bruyne'}

# Pop Dictionary (Berdasarkan Key)
dataFoden = data.pop('c')
print(f"Ini adalah 'c' \t\t: {dataFoden}") # Output : Ini adalah 'c' : Foden
print(f"Ini adalah Data \t: {data}") # Output : Ini adalah Data : {'a': 'Alvarez', 'b': 'Kovacic', 'd': 'De Bruyne'}

# Popitem Dictionary (Data Paling Terakhir)

dataLast = data.popitem()
print(f"Ini adalah terakhir \t: {dataLast}") # Output : Ini adalah terakhir : ('d', 'De Bruyne')
print(f"Ini adalah Data \t: {data}") # Output : Ini adalah Data : {'a': 'Alvarez', 'b': 'Kovacic', 'c': 'Foden'}
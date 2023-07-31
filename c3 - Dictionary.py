# List = array, mengakses menggunakan index
# Dictionary (dict) = associative array
# identifier > key

list = ['MrBeast','Jimmy','Neutron']
dict = {
    'ab':'Tukul',
    'cd':'Maeng',
    'ef':'Ellay',
    'gh': 21,
    'ij': list
}
print(dict['ef']) # Output : Ellay
print(dict['ij']) # Output : ['MrBeast', 'Jimmy', 'Neutron']
print(dict['gh']) # Output : 21
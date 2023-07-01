# Integer (angka satuan)
data_integer = 7_000
print("Nilainya adalah", data_integer, "dan bertipe data", type(data_integer))

# Float (angka koma)
data_float = 21.9
print("Nilainya adalah", data_float, "dan bertipe data", type(data_float))

# String (kumpulan karakter)
data_string = "Daiva"
print("Tulisan ini adalah", data_string, "dan bertipe data", type(data_string))

# Boolean (true/false)
data_bool = True
print("Tulisan ini adalah", data_bool, "dan bertipe data", type(data_bool))

# Complex (khusus)
data_complex = complex(21,9)
print("Nilainya adalah", data_complex, "dan bertipe data", type(data_complex))

# CONTOH
# C Double (import dari bahasa C)
from ctypes import c_double

data_c_double = c_double(21.9)
print("Nilainya adalah", data_c_double, "dan bertipe data", type(data_c_double))
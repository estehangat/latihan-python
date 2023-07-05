# Mengubah tipe data
# int, float, str, bool

## INTEGER
print("*****INTEGER*****")
data_int = 7
print("Nilai data tersebut adalah", data_int, "dan bertipe", type(data_int))

data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int) # False jika 0
print("Nilai data tersebut adalah", data_float, "dan bertipe", type(data_float))
print("Nilai data tersebut adalah", data_string, "dan bertipe", type(data_string))
print("Nilai data tersebut adalah", data_bool, "dan bertipe", type(data_bool))

# Output : 
# *****INTEGER*****
# Nilai data tersebut adalah 7 dan bertipe <class 'int'>
# Nilai data tersebut adalah 7.0 dan bertipe <class 'float'>
# Nilai data tersebut adalah 7 dan bertipe <class 'str'>
# Nilai data tersebut adalah True dan bertipe <class 'bool'>

## FLOAT
print("*****FLOAT*****")
data_float = 21.7
print("Nilai data tersebut adalah", data_float, "dan bertipe", type(data_float))

data_int = int(data_float) # Dibulatkan ke bawah
data_string = str(data_float)
data_bool = bool(data_float) # False jika 0
print("Nilai data tersebut adalah", data_int, "dan bertipe", type(data_int))
print("Nilai data tersebut adalah", data_string, "dan bertipe", type(data_string))
print("Nilai data tersebut adalah", data_bool, "dan bertipe", type(data_bool))

# Output :
# *****FLOAT*****
# Nilai data tersebut adalah 21.7 dan bertipe <class 'float'>
# Nilai data tersebut adalah 21 dan bertipe <class 'int'>
# Nilai data tersebut adalah 21.7 dan bertipe <class 'str'>
# Nilai data tersebut adalah True dan bertipe <class 'bool'>

## STRING
print("*****STRING*****")
data_string = "7"
print("Nilai data tersebut adalah", data_string, "dan bertipe", type(data_string))

data_int = int(data_string) # String harus angka
data_float = float(data_string) # String harus angka
data_bool = bool(data_string) # False jika string kosong
print("Nilai data tersebut adalah", data_int, "dan bertipe", type(data_int))
print("Nilai data tersebut adalah", data_float, "dan bertipe", type(data_float))
print("Nilai data tersebut adalah", data_bool, "dan bertipe", type(data_bool))

# Output :
# *****STRING*****
# Nilai data tersebut adalah 7 dan bertipe <class 'str'>
# Nilai data tersebut adalah 7 dan bertipe <class 'int'>
# Nilai data tersebut adalah 7.0 dan bertipe <class 'float'>
# Nilai data tersebut adalah True dan bertipe <class 'bool'>

## BOOLEAN
print("*****BOOLEAN*****")
data_bool = True
print("Nilai data tersebut adalah", data_bool, "dan bertipe", type(data_bool))

data_int = int(data_bool) # Dibulatkan ke bawah
data_float = float(data_bool) 
data_string = str(data_bool) 
print("Nilai data tersebut adalah", data_int, "dan bertipe", type(data_int))
print("Nilai data tersebut adalah", data_float, "dan bertipe", type(data_float))
print("Nilai data tersebut adalah", data_string, "dan bertipe", type(data_string))

# Output :
# *****BOOLEAN*****
# Nilai data tersebut adalah True dan bertipe <class 'bool'>
# Nilai data tersebut adalah 1 dan bertipe <class 'int'>
# Nilai data tersebut adalah 1.0 dan bertipe <class 'float'>
# Nilai data tersebut adalah True dan bertipe <class 'str'>

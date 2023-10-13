# Las funciones build_in son funciones integradas en el lenguaje de Python, 
# podemos utilizarlas como queramos y no necesitamos entender su lógica interna.

numbers = [4, 7, 1, 42, 15]

#* Encontrando el número mayor de un iterable. max()
max_number = max(numbers)
print(max_number) # 42

#* Encontrando el número menor de un iterable. min()
min_number = min(numbers)
print(min_number) # 1

#* Redondeando a 6 decimales. round()
# El primer argumento es el número a redondear, y el segundo es el número de decimales, por defecto es 0
float_number = 12.435734597
round_number = round(float_number, 3)
print(round_number)

#* bool() --> Devuelve: 
#* False cuando le pasemos: 0, dato vacío, False o None
#* True cuando le pasamos un número distinto a 0, True, Datos no vacíos
result = bool(0)
print(result) # False
result = bool()
print(result) # False
result = bool([])
print(result) # False
result = bool(())
print(result) # False
result = bool(None)
print(result) # False
result = bool(False)
print(result) # False
result = bool(2132)
print(result) # True
result = bool([34, 'hola'])
print(result) # True

#* all() retorna True cuando todos los valores de un iterable son True
# Igual que boo() pero con listas de elementos
result_all = all([423, True, 'buenas', ['faksgnj', 0]]) 
print(result_all) # True
result_all = all([0, True, 'buenas', ['faksgnj', 0]]) 
print(result_all) # False, el primer elemento es 0 --> False

#* sum() Suma todos los valores de un iterable. Solo funciona con numeros
result_sum = sum(numbers)
print(result_sum)
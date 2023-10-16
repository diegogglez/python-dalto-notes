
#* Forma no óptima de sumar valores
# def suma(list):
#   count = 0
#   for number in list:
#     count += number
#   return count

# print(sum([4, 6, 6, 23]))

#* Utilizando el operador * como argumento (*args)
# Este parámetro debe ser el ultimo parametro de la función, porque es una lista indefinida
def suma(name, *numbers): # Con el * delante, convertimos todos los parámetros que pasemos a uno solo
  print(numbers) # (3, 4, 5, 65) --> genera una tupla con los numeros que le pasamos al llamar la función
  return f'{name}: la suma de tus números es: {sum(numbers)}'

result = suma('Diego', 3, 4, 5, 65)
print(result) # Diego: la suma de tus números es: 77 
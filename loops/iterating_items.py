# En Python se usa el bucle 'for in'
# TODOS ESTOS BUCLES FUNCIONAN IGUAL PARA LISTAS, TUPLAS y CONJUNTOS.

animals = ['perro', 'gato', 'loro', 'cocodrilo']
numbers = [10, 23, 12, 70]

#* Iterando la lista 'animals'
for animal in animals:
  print(animal)
  # perro                                                                                                                                                   
  # gato                                                                                                                                                    
  # loro                                                                                                                                                    
  # cocodrilo
  
  
#* Iterando la lista 'numbers' y multiplicando cada valor por 100
for number in numbers:
  result = number * 10
  print(result)
  # 100
  # 230
  # 120
  # 700
  
#* Iterando las dos listas a la vez con zip()
# Funciona con 2 o más listas
# Para usar esta función las dos listas deben tener la misma longitud, o se perderán valores
for number, animal in zip(animals, numbers):
  print(f'recorriendo lista animals: {animal}')
  print(f'recorriendo lista numbers: {number}')
  # recorriendo lista animals: 10
  # recorriendo lista numbers: perro
  # recorriendo lista animals: 23
  # recorriendo lista numbers: gato
  # recorriendo lista animals: 12
  # recorriendo lista numbers: loro
  # recorriendo lista animals: 70
  # recorriendo lista numbers: cocodrilo
  

#* Iterando con la función range()
# Itera entre los valores comprendidos entre el primer y el segundo parámetro que le pasemos, arranca en el primero y termina uno antes del segundo
# Si solo ponemos un parámetro, va desde el 0 hasta uno menos que el valor

for number in range(5, 10):
  print(number)
  # 5
  # 6
  # 7
  # 8
  # 9

for number in range(10):
  print(number)
  # 0
  # 1
  # 2
  # 3
  # 4
  # 5
  # 6
  # 7
  # 8
  # 9
  
# Podemos usar esta función para recorrer listas por el índice
#! Esta forma no es óptima (Y no funciona en conjuntos --> TypeError: 'set' object is not subscriptable)
for number in range(len(numbers)):
  print(numbers[number])
  # 10
  # 23
  # 12
  # 70
  
#* Forma correcta de recorrer una lista por el índice con enumerate().
# Esta función nos devuelve una tupla
for number in enumerate(numbers):
  print(number)
  # (0, 10)
  # (1, 23)
  # (2, 12)
  # (3, 70)
  
for number in enumerate(numbers):
  index = number[0]
  value = number[1]
  print(f'index: {index}, value: {value}')
  # index: 10, value: 0
  # index: 23, value: 1
  # index: 12, value: 2
  # index: 70, value: 3

#? La solución más elegante y práctica es desempequetar la tupla directamente en el for:
for number, i in enumerate(numbers):
  print(f'index: {i}, value: {number}')
  # index: 10, value: 0
  # index: 23, value: 1
  # index: 12, value: 2
  # index: 70, value: 3
  
#* Usando el for/else:
# El else se ejecuta al terminar el bucle. SIEMPRE se ejecuta
for number in numbers:
  print(f'Ejecutando el valor actual del bucle: {number}')
else: 
  print('El bucle terminó')
  # Ejecutando el valor actual del bucle: 10
  # Ejecutando el valor actual del bucle: 23
  # Ejecutando el valor actual del bucle: 12
  # Ejecutando el valor actual del bucle: 70
  # El bucle terminó
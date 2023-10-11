frutas = ['banana', 'manzana', 'ciruela', 'pera', 'naranja', 'granada', 'durazno']
cadena = 'Hola Dalto'
numeros = [2, 5, 8, 10]

#* Evitando que se coma una manzana con la sentencia 'continue'
for fruta in frutas:
  if fruta == 'granada':
    continue # El 'continue' salta esa iteracion cuando se cumple el if
  print(f'Me voy a comer una {fruta}')
  # Me voy a comer una banana                                                                                                                                              
  # Me voy a comer una manzana                                                                                                                                             
  # Me voy a comer una ciruela
  # Me voy a comer una pera
  # Me voy a comer una naranja
  # Me voy a comer una durazno
 
#* Evitando que el bucle siga ejecutandose con break
for fruta in frutas:
  if fruta == 'pera':
    break # El 'break' termina el bucle cuando se cumple el if. tras un break no se ejecuta nada más (el else tampocos)
  print(f'Me voy a comer una {fruta}')
  # Me voy a comer una banana
  # Me voy a comer una manzana
  # Me voy a comer una ciruela
  
print('bucle terminado')

#* Iterando una cadena de texto
for letra in cadena:
  print(letra)
  # H
  # o
  # l
  # a
  #
  # D
  # a
  # l
  # t
  # o

#* For en una sola línea de código
#? Método tradicional:
# numeros_duplicados = list() # Lista vacía
# for numero in numeros:
#   numeros_duplicados.append(numero * 2)

#? En una sola línea:
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados) # [4, 10, 16, 20]
  

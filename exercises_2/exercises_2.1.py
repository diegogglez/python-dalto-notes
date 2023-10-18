
#* Faltó el profe y los pibes van a armar la clase
#* Uno de los alumnos va a ser el profesor y otro el asistente

#* (A) --> Pedir los nombres y la edad de los compañeros que vinieron a clase y ordenar los datos de mayor a menor
#* (B) --> El mayor de la clase será el Profesor y el menor el Asistente.

def obtener_compañeros(cantidad):
  # Definimos una lista vacía
  compañeros = []
  # Hacemos una iteración con range() en base a la cantidad de compañeros
  for i in range(cantidad)  :
    # Definimos el nombre y la edad de cada uno mediante inputs por consola
    nombre = input('ingrese el nombre del compañero: ')
    edad = int(input('Ingrese la edad del compañero: '))
    # Generamos una tupla con el nombre y la edad de cada compañero y lo metemos en la lista 'compañeros'
    compañero = (nombre, edad)
    compañeros.append(compañero)
  # Con short ordenamos de manera ascendente. la key es el criterio de ordenación
  #? En este caso, con una función lambda retornamos el valor del segundo parámetro de cada 
  #? tupla en cada interacción, es decir: la edad.
  compañeros.sort(key = lambda x: x[1]) 
  asistente = compañeros[0][0]
  profesor = compañeros[-1][0] # Con [-1] accedemos al último elemento
  
  return asistente, profesor

asistente, profesor = obtener_compañeros(5)

print(f'El profesor es: {profesor} y su asistente es: {asistente}')

# ingrese el nombre del compañero: Lucas                                                                                                        
# Ingrese la edad del compañero: 12                                                                                                             
# ingrese el nombre del compañero: Maria
# Ingrese la edad del compañero: 13
# ingrese el nombre del compañero: Juan
# Ingrese la edad del compañero: 11
# ingrese el nombre del compañero: Veronica
# Ingrese la edad del compañero: 24
# ingrese el nombre del compañero: Diego
# Ingrese la edad del compañero: 16
# El asistente es: Juan
# El profesor es: Veronica
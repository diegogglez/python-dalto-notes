
#* Creando una función de 3 parametros
# def frase(nombre, apellido, adjetivo): # Parametros de posición
  # return f'Hola {nombre} {apellido}, sos un {adjetivo}'

#* Utilizando keyword arguments
# Con esta sintaxis estamos 'forzando los argumentos' y así podemos alterar su orden
# frase_resultante = frase(adjetivo = 'capo', nombre = 'Diego', apellido = 'García') # Parámetros de clave - valor
# print(frase_resultante)

#* Creando la función con un parámetro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo = 'tonto'): #adjetivo es opcional y por defecto será 'tonto' si no lo introducimos
  return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase('Diego', 'García')
print(frase_resultante) # Hola Diego García, sos un tonto
frase_resultante2 = frase('Diego', 'García', 'inteligente') # Al introducir el tercer parámetro, cambiamos su valor por defecto al que queramos
print(frase_resultante2) # Hola Diego García, sos muy inteligente  
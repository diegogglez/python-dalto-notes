
#* Creando una función simple
# def saludar():
  # print('Hola Lucas, mi maestro ¿cómo andas?')
  
#* Ejecutando la función simple 
# saludar()

#* Creando una función con parámetros
def saludar(name, sex):
  sex = sex.lower() # Pasamos la cadena 'sex' a lowercase
  if (sex == 'mujer'):
    adjetivo = 'reina'
  elif (sex == 'hombre'):
    adjetivo = 'titan'
  else:
    adjetivo = 'amor'
  
  print(f'Hola {name}, mi {adjetivo} ¿Cómo andas?')
  

saludar('Diego', 'Hombre')
saludar('Yal', 'Mujer')
saludar('Diego', 'no binario')

#* Creando una función que nos retorne valores
# Retornar valores nos permite guardarlos en una variable y operar con ella desde fuera de la función
def crear_contraseña(num):
  chars = 'abcdefghij' # Declaramos un string de 10 caracteres
  num_string = str(num) # Convertimos el parámetro num a string
  num = int(num_string[0]) # Nos quedamos con el primer dígito del parámetro num
  # generamos 3 números para definir los caracteres que va a tener la contraseña
  c1 = num - 2
  c2 = num
  c3 = num - 5
  # Generamos la contraseña con los caracteres anteriores y el parámetro num * 2
  contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}'
  return contraseña, num

mi_contraseña, primer_numero = crear_contraseña(46) # (cej8, 4)
frase = f'tu nueva contraseña es {mi_contraseña} y el primer dígito introducido es {primer_numero}'
print(frase)
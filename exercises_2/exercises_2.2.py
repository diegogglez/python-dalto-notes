# En matemáticas, un número primo es un número natural mayor que 1 que tiene únicamente dos divisores 
# positivos distintos: él mismo y el 1

#* Crear una función que al pasarle un número, nos devuelva todos los números primos 
#* comprendidos entre 2 y el número dado

# Comprobamos si es primo dividiendolo por todos los números entre 2 y el número dado menos 1
def es_primo(num):
  for i in range(2, num - 1):
    if num % i == 0: return False
  return True

def primos_hasta(num):
  primos = []
  for i in range(3, num + 1): # descartamos el 0 y el 2 e incluimos el número introducido en la comprobacion
    result = es_primo(i)
    if result == True: primos.append(i)
  return primos

resultado = primos_hasta(98)

print(resultado) # [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 
      
  
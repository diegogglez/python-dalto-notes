
#? Las lambda functions serían el equivalente a las arrow functions de javascript

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#* Normalmente declaramos funciones así:
# def nombre_funccion(parametros):
  # Instrucciones de código

#* Creando una función lambda para multiplicar por dos
# lambda crea funciones anonimas, que después podemos almacenar en variables:
# Con esto evitamos abrir un nuevo bloque de código
# Retornan automaticamente sin el 'return'
# No sirven si tenemos que dar más de una instrucción
double = lambda x : x * 2
print(double(5)) # 10

#* Creando una función que nos diga si el numero es par o no:
def is_even(num):
  if (num % 2 == 0):
    return True
  
#* Usando filter con una función común
# filter() es una build in function que ejecuta la función que pasamos como primer argumento, 
# para cada uno de los valores del iterable que pasamos como segundo argumento
even_numbers= filter(is_even, numbers)
print(list(even_numbers)) # [2, 4, 6, 8]

#* Creando la misma funcion con lambda
# Creamos la función en la misma linea que declaramos el filter
even_numbers_2 = filter(lambda number: number % 2 == 0, numbers)
print(list(even_numbers_2)) # [2, 4, 6, 8]

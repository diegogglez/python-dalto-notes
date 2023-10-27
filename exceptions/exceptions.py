# Un Evento es cualquier cosa que suceda en el programa, mover el raton, hacer click, teclado...
# Las excepciones también son eventos, pero son eventos que detienen la ejecución del programa

#* creando una función que pide dos números por consola y los suma
def sum_two():
  # Iniciamos un bucle
  while True:
    a = input('Numero 1: ')
    b = input('Numero 2: ')
    try: # Primero siempre se intenta ejecutar el try
      result = int(a) + int(b)
    # Todas las excepciones son derivados de una clase o subclase de Exception
    except Exception as e: # si el try no se puede resolver, se ejecuta el except y vuelve a empezar el bucle
      print('Te pedi un numero salame, no te hagas el gracioso')     
      print(f'ERROR: {e}')     
    else: # El else solo se ejecuta cuando no se ejecuta el except y viceversa
      break # Corta el bucle
    finally: # finally se va a ejecutar siempre al final independientemente de lo que pase antes
      print('Manejo de exceptión finalizado')
  return result

print(sum_two())
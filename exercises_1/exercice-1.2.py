# Si en promedio, una persona dice 2 palabras por segundo.
# (A) pídele al usuario un texto y muestra por consola la cantidad de palabras del texto y cuanto tardaría en decirlo
# (B) Si se tarda más de 1 minuto decirle: 'Para flaco tampoco te pedí un testamento'
# (c) Dalto habla un 30% más rápido, ¿Cuanto tardaría él en decirlo?

# Le pedimos al usuario que nos diga una frase
sentence = input('Decime una frase y te calculo cuanto tardarías si tuvieras que decirla: ')

# Creamos una lista con todas las palabras
words_split = sentence.split(' ')

# Usamos len() para saber el número de palabras
total_words = len(words_split)

# Si tarda más de un minuto en decirlo, le decimos que pare un poco
if total_words > 120: 
  print('Para flaco tampoco te pedí un testamento')
  
# Mostramos cuanto tardaría en decir las palabras
print(f'Dijiste {total_words} palabras, y tardarás {total_words / 2} segundos en decirlo')
print(f'Dalto lo diría en {total_words / 2 - total_words / 2 * 0.3} segundos')
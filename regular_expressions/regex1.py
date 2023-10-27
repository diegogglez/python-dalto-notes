import re

text = 'The quick brown fox jumps over the lazy dog'

# Buscamos una cadena donde:
# 'The' aparezca al principio '^' 
# seguido de un espacio en línea '.'
# con el '*' estamos bucando la mayor cantidad de coincidencias para la sentencia de la izq, 
# si no encuentra coincidencias tambien lo permite
# la al final de la cadena debe de encontrar 'dog'

x = re.search('^The.*dog$', text)

if x:
  print('SI')
else:
  print('NO')
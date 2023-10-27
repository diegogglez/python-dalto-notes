import re

email = 'example@example.com'

# valido aquello que contenga:
# caracteres de la a a la z, de la A a la Z y del 0 al 9
# que no contenga espacios en linea y '_' tambien esta permitido
# el % indica que validatodo lo que vaya antes y despues de este
# el + busca 1 o más coincidencias, afecta a lo que tiene a la izq
# despues tiene que ir un @ seguido del mismo patron
# con \. buscamos que haya un .
# despues del punto a de haber caracteres de a a Z y de A a Z, almenos dos caracteres y sin un límite máximo
# No existen dominios de un solo caracter
pattern = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

result = re.match(pattern, email)

if result:
  print('Dirección de correo válida')
else:
  print('Dirección de correo inválida!')
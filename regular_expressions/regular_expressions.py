import re # Módulo standard de Python para expresiones regulares

text = '''Hola maestro. ¿Cómo estás mi capitán? (esta es la cadena 1)
Esta es la línea 234 de texto.
Esta es la abblínea 2. de textoababb.
Esta es la línea 2. de texto.
Y esta es la final (linea 3) definitiva my capitán'''

#* Haciendo una búsqueda simple
# result = re.findall('es', text, flags=re.IGNORECASE) # con el tercer parámetro podemos ignorar las mayusculas

#* \d --> Busca dígitos numéricos del 0 al 9
# result = re.findall(r'\d', text) # Con la 'r' indicamos que vamos a usar expresiones regulares

#* \D --> Busca TODO MENOS dígitos numéricos del 0 al 9
# result = re.findall(r'\D', text) 

#* \w --> Busca caracteres alfanuméricos [a-z A-Z 0-9 _] (En Python el '_' se considera un caracter alfanumérico)
# result = re.findall(r'\w', text) 

#* \W --> Busca TODO MENOS caracteres alfanuméricos [a-z A-Z 0-9 _] (En Python el '_' se considera un caracter alfanumérico)
# result = re.findall(r'\W', text) 

#* \s --> Busca espacios en blanco (espacios comunes, tabs, saltos de línea)
# result = re.findall(r'\s', text) 

#* \S --> Busca TODO MENOS espacios en blanco (espacios comunes, tabs, saltos de línea)
# result = re.findall(r'\S', text) 

#* . --> Busca TODO MENOS saltos de línea
# result = re.findall(r'.', text) 

#* \n --> Busca saltos de línea
# result = re.findall(r'\n', text) 

#* \. --> Cancelamos caracteres especiales (todos los que no son alfanuméricos)
# Cancelamos la función del punto y buscando puntos
# result = re.findall(r'\.', text)

#* armando una cadena que busque un numero, seguido de un punto y un espacio 
# result = re.findall(r'\d\.\s', text)
# print(result) # ['2. ']  

#* ^ --> Busca el comienzo de una línea
# Buscando 'Hola' al principio de la linea
# Si usamos flags=re.M busca en todos los inicios de salto de línea, si no solo busca en el comienzo de la cadena total
# result = re.findall(r'^Esta', text, flags=re.M)
# print(result) # ['Esta', 'Esta', 'Esta']   

#* $ --> Busca el final de una línea
# result = re.findall(r'capitán$', text)
# print(result)  

#* {n} --> Busca n cantidad de veces el valor de la izquierda
# con esta expresion estamos buscando 3 valores numéricos concatenados seguidos de un espacio
# result = re.findall(r'\d{3}\s', text)
# print(result) # ['234 '] 

#* {n,m} --> Busca almenos n cantidad de veces y como máximo m cantidad de veces
# result = re.findall(r'\d{1,2}', text)
# print(result) # ['1', '23', '4', '2', '2', '3']

#* {n,m} --> Busca almenos n cantidad de veces y como máximo m cantidad de veces
# Estamos buscando el conjunto 'ab' donde se repita almenos una vez y máximo 2 veces
# result = re.findall(r'(ab){1,2}', text) # podemo buscar conjuntos de caracteres agrupados por ()
# print(result) # ['ab', 'ab'] 

#* | --> Busca una cosa o la otra, con que alguna se cumpla ya devuelve un objeto
# estamos buscando |d{2,3} O la cadena 'cap'
result = re.findall(r'\d{2,3}|cap', text)
print(result) # ['cap', '234', 'cap']   





string1 = 'Hola soy Dalto'
string2 = 'Bienvenido maquinola'

#! Todos los metodos son funciones pero no todas las funciones son métodos. Los métodos son funciones que 
#! se aplican a un objeto.

#* DIR --  FUNCIÓN que devuelve la lista de atributos/métodos válidos para el elemento que le pasamos como parámetro
# print(dir(string1))

#* UPPER -- MÉTODO que convierte el string a mayúsculas, la sintaxis de los métodos es: elemento.método()
mayusc = string1.upper()

#* LOWER -- convierte a minúscula
minusc = string1.lower()

#* CAPITALIZE -- convierte la primera letra a mayúscula. El resto las convierte a minúsculas aun que estén en mayúscula
primera_letra_mayusc = string1.capitalize()

#* FIND -- Busca un string en otro string. devuelve la posición del elemento encontrado. Si no lo encuentra devuelve -1
busqueda_find = string1.find('a') # devuelve 3, el caracter 3 está en la posición 3 del string1 'Hol(a)...'

#* INDEX -- Busca un string en otro string. Si no encuentra nada tira un Exception, un error
busqueda_index = string1.index('D')

#* ISNUMERIC -- Si es numérico devuelve True, si no False
string_numerico = '5463542'
es_numerico = string_numerico.isnumeric() # True
es_numerico = string1.isnumeric() # False

#* ISALPHA -- Si es alfanumérico devuelve True, si no devuelve False
# Solamente admite caracteres A-Z, no incluye espacios, números o caracteres especiales
string_alphanumerico = 'hola'
string_no_alphanumerico = 'hola buenas tardes'

es_alphanumerico = string_alphanumerico.isalpha() # True
es_alphanumerico2 = string_no_alphanumerico.isalpha() # Fasle

#* COUNT -- Devuelve el numero de occurrencias en la cadena dada (cuantas veces encontró una coincidencia)
contar_coincidencias = string1.count('a') # 2 (la letra 'a' se repite 2 veces)
contar_coincidencias = string1.count('x') # 0 (si no encuentra nada, devuelve 0)

#* LEN -- Devuelve la cantidad de caracteres del string. NO ES UN MÉTODO, ES UNA FUNCIÓN
contar_caracteres = len(string1)

#* STARTSWITH -- verificamos si un string empieza con otro string dado.
empieza_con = string1.startswith('Hola') # True
empieza_con = string1.startswith('6') # False

#* ENDSWITH -- verificamos si un string termina con otro string dado.
termina_con = string1.endswith('to') # True
termina_con = string1.endswith('fasf') # False

#* REPLACE -- remplaza un trozo del string dado por otro dado
# Si NO encuentra coincidencias, devuelve el string original
cadena_nueva = string1.replace('la', 'lu') # reemplazamos 'la' por 'lu', devuelve 'Holu soy Dalto'

#* SPLIT -- Nos devuelve una matriz/array. Separa un string con el string que le pasemos. Igual que en JavaScript
cadena = '1,2,3'
cadena_separada = string1.split() # ['Hola', 'soy', 'Dalto'] si no pasamos nada, separa por espacios
cadena_separada = cadena.split(',') # ['1', '2', '3']  
# Si no encuentra coincidencias, crea un array de longitud 1, con toda la cadena como primer elemento

print(cadena_separada)
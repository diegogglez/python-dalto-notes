
#* Creando diccionarios con dict()
# Si queremos crear un diccionario vacío solo podemos de esta manera. (Se aplica para todos los datos compuestos)
dict = dict(name='Lucas', lastname='Dalto')

#* Las listas no pueden ser claves porque son mutables. Podemos usar tuplas o frozenset para conjuntos.
dict = {('dalto', 'rancio'): 'jajajs'} 
print(dict) #? {('dalto', 'rancio'): 'jajajs'}
dict = {frozenset(['dalto', 'rancio']): 'jajajs'} 
print(dict) #? {frozenset({'rancio', 'dalto'}): 'jajajs'} 
# dict = {['dalto', 'rancio']: 'jajajs'} # Error unhashable type: 'list'
# dict = {{'dalto', 'rancio'}: 'jajajs'} # Error unhashable type: 'set'

#* Creando diccionarios con fromkeys()
# crea keys iterando el primer elemento, y todas con el segundo elemento como value, por defecto es 'none'
dict = dict.fromkeys('name', 'lastname')
print(dict) # {'n': 'lastname', 'a': 'lastname', 'm': 'lastname', 'e': 'lastname'} 

#También podemos una lista como primer elemento iterable
dict = dict.fromkeys(['name', 'lastname'], 'ni idea hulio')
print(dict) # {'name': 'ni idea hulio', 'lastname': 'ni idea hulio'}

# Podemos iterar una cadena de texto para generar las keys
dict = dict.fromkeys('abcde') 
print(dict) # {'a': None, 'b': None, 'c': None, 'd': None, 'e': None}

# Si introducimos los parametros como una lista, nos genera las claves con valor 'none'
dict = dict.fromkeys(['name', 'lastname'])
print(dict) # {'name': None, 'lastname': None}


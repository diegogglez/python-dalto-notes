
#* Declarando una list, se puede modificar
list = ['Diego García', 'González', 27, 1.86, True]
print(list);

#* declarando un tuple, no se puede modificar
# Solo podemos buscar elementos y usar el index()
tuple = ('Diego García', 'González', 27, 1.86, True)
print(tuple)
# Esto es válido
# list[3] = 'maquinola'

# Esto no
# tuple[3] = 'maquinola'

#* declarando un conjunto (set)
# Se puede redefinir/reconstruir el conjunto completo, pero no podemos alterar elementos concretos como en la lista.
# En este sentido se comporta como las tublas.
# No almacena valores duplicados, si los encuentra, los suprime (?).
# Se puede iterar con un bucle, pero no podemos acceder a el por un índice.
# Son datos desordenados
set = {'Diego García', 'González', 27, 1.86, True, 'González'}
set = {'Diego García', 'González', 27, 1.86, True,}
print(set)

# print(set[3]) -> no puede acceder al elemento por su íncide

#* Declarando un diccionario (dict)
# Es igual que un JSON en JavaScrip. Estructura key: value
# Los datos también estan desordenados
dict = {
  'nombre': 'Lucas Dalto',
  'canal': 'Soy Dalto',
  'esta_emocionado': True,
  'altura': 1.84,
  'dato_duplicado': 'Soy Dalto'
}

print(dict['nombre'])
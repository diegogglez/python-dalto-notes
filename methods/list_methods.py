
#* LIST -- Función para crear una lista
my_list = list(['hola', False, 34, 56, 2])

#* LEN -- Función que devuelve la cantidad de elementos de una lista
number_of_items = len(my_list)

#* APEND -- Agrega un elemento al final de la lista
my_list.append(True)

#* INSERT -- Agrega un elemento a la lista con un índice específico
my_list.insert(2, 'toma mama') # En la posición 2, agrega 'toma mama'

#* EXTEND -- Agrega varios elementos a la lista
my_list.extend([False, 2030]) # se tiene que pasar una lista como parámetro

#* POP -- Eliminamos un elemento de una lista, por su índice
my_list.pop(0) # Eliminamos el elemento 0 ('hola')
my_list.pop(-1) # -1 para eliminar el último elemento, -2 para eliminar el penúltimo y asi sucesivamente

#* REMOVE -- Elimina un elemento de la lista por su valor
# Si le pasamos un parámetro que no encuentra, nos da error
my_list.remove('toma mama')

#* CLEAR -- Elimina todo
# my_list.clear()

#* SORT -- Ordena los elementos de manera ascendente. No admite strings
# los elementos False van primero, despues los True, y luego los numeros en orden
my_list.sort()
my_list.sort(reverse=True) # Ordenamos los elementos en orden inverso o descendente, ahora False va de último, True penultimo...

#* REVERSE -- Invierte los elementos, pero no por orden descendente, hace el inverso al existente.
my_list.reverse()

#* INDEX -- devuelve la posición del elemento, que pasamos como parámetro, en la lista
# Si no lo encuentra tira un error "'item' is not in list"
item = my_list.index(435)

print(item)
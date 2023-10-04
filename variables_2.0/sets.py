
#* DIFERENTES FORMAS DE CREAR UN CONJUNTON SET

#* Creando un conjunto con set()
# nos crea un conjunto mutable (podemos añadir y quitar elementos)
set = set(['dato 1', 'dato2']) 

#* Creando un conjunto con frozenset()
# nos crea un conjunto inmutable (no podemos añadir ni crear elementos)
set1 = frozenset(['dato1', 'dato2']) 

#* Metiendo un conjunto dentro de otro conjunto
#! CONCEPTO HASH TABLE
#! Una tabla hash es una estructura de datos que guarda el tipo de dato abastracto llamado diccionario, 
#! Este asocia claves (keys) con valores (value)
#! Se dice que un elemento es 'unhashable' cuando no puede utilizarse como key en una tabla
#! un objeto es 'hashable' cuando posee un 'hash value' que se mantiene constante a lo largo de su ciclo de vida y por tanto 
#! pueden utiizarse como key dentro de un diccionario o un elemento en un set

#? Hashable types in Python typically include immutable types like integers, floats, strings, tuples, and frozensets. 
#? These types have a fixed value and can be hashed, meaning their hash value can be calculated and used as an index in a hash table.

#? On the other hand, mutable types like lists, sets, and dictionaries are not hashable because they can be modified, 
#? and their hash value could change. If you try to use a mutable object as a key in a dictionary or as an element in a set, 
#? Python will raise a TypeError stating that the object is an "unhashable type."

# Por tanto, si queremos meter un conjunto dentro de otro, tenemos que usar una tupla o un frozen set
set2 = {set1, 'dato3'} # Estamos metiendo un frozenset dentro de un set -> {'dato3', frozenset({'dato2', 'dato1'})}
set3 = {('dato1', 2), 'dato3'} # Estamos metiendo una tupla dentro de un set -> {('dato1', 2), 'dato3'} 


#* TEORÍA DE CONJUNTOS
# Cuando tenemos un conjunto A dentro de un conjunto B, 
# se dice que A es un subconjunto de B y B es un Superconjunto de A

set4 = {1, 3, 5, 7}
set5 = {1, 3, 7}

#* Comprobando si un conjunto es un subconjunto de otro con issubset()
result = set5.issubset(set4) # True
result2 = set4.issubset(set5) # False
# Podemos hacer la misma comprobación usando <=. No tiene que ver con la cantidad de datos
result3 = set5 <= set4 # True
result4 = set4 <= set5 # False

#* Comprobando si un conjunto es un superconjunto de otro con issuperset()
result5 = set4.issuperset(set5) # True
result6 = set5.issuperset(set4) # False
# Podemos hacer la misma comprobación usando >
result7 = set4 > set5 # True
result7 = set5 > set4 # False

#* Comprobando si hay un dato en comun con isdisjoint()
# Esta función retorna True solo cuando los conjuntos que se comparan no tienen ningun valor en común
result8 = set5.isdisjoint(set4) # False

print(result8)
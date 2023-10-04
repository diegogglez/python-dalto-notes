# El desempaquetado funciona tanto para listas como para tuplas

# Creando paquetes de datos
data_tuple = ('Lucas', 'Dalto', 1000000)
data_list = ['Lucas', 'Dalto', 1000000]

# Esta es la sintaxis para desencapsular variables.
#* La cantidad de variables debe ser igual a la cantidad de elementos de la lista
name, lastname, subs = data_list

# Mostrando resultados
print(subs)
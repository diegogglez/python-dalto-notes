
#* DIFERENTES FORMAS DE CREAR UNA TUPLA
# Las tuplas se usan cuando manejamos datos de 'solo lectura'.
# el uso de la memoria es más eficiente que el de una lista.

#* Creando una tupla con tuple()
my_tuple = tuple(['dato1', 'dato2', '...'])

#* Creando una tupla sin paréntesis de múltiples datos:
# Cuando ya hay multiples valores no es necesaria la coma final
my_tuple_2 = 'dato1', 'dato2', '...' # Es lo mismo que: my_tuple_2 = ('dato1', 'dato2', '...')

#* Creando una tupla sin paréntesis de un solo dato:
# Ponemos la coma al final, si no sería un string en este caso
my_tuple_3 = 'dato1', 

print(type(my_tuple_3))
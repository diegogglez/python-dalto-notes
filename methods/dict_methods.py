my_dict = {
  'name': 'Lucas',
  'lastname': 'Dalto',
  'subs': 1000000
}

#* keys() nos devuelve las claves del diccionario. 
# También nos sirve para iterar
my_keys = my_dict.keys()

#* get() Retorna el valor de la key que le pasemos
# Si no encuentra nada, devuelve 'none'
name = my_dict.get('name') # 'Lucas'
lastname = my_dict.get('lastname') # 'Dalto'
subs = my_dict.get('subs') # 1000000

#* cleat() Elimina todos los elementos del diccionario
# my_dict.clear()
# print(my_dict) # {}

#* pop() Elimina un elemento del diccionario, por la key
my_dict.pop('name') # Elimina el elemento 'name' con valor 'Lucas'
# my_dict.pop('name', 'subs') # Podemos eliminar varios elementos a la vez

#* items() Nos retorna el diccionario como una lista iterable
my_iterable_dict = my_dict.items()

print(my_iterable_dict)
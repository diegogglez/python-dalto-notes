dict = {
  'name': 'Lucas',
  'lastname': 'Dalto',
  'subs': 1000000
}

#* el bucle for nos devuelve las keys
for key in dict:
  print(key)
  # name                                                                                                                                                    
  # lastname                                                                                                                                                
  # subs
 
#* Con la función items(), nos devuelve cada key-value en una tupla
for key in dict.items():
  print(key) 
  # ('name', 'Lucas')
  # ('lastname', 'Dalto')
  # ('subs', 1000000)
  
#* Podemos usar el desempaquetado para acceder a las claves y valores  
for key, i in dict.items():
  print(f'Recorriendo diccionario, la clave es: {key} y el value es: {i}')
  # Recorriendo diccionario, la clave es: name y el value es Lucas
  # Recorriendo diccionario, la clave es: lastname y el value es Dalto
  # Recorriendo diccionario, la clave es: subs y el value es 1000000
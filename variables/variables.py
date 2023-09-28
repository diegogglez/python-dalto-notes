
#* DECLARANDO UNA VARIABLE
a = 2
b = 3
c = a + b
name = 'Diego'
fullName = 'Diego García' # camelCase (como en JavaScript)
full_name = 'Diego García' #? snake_case (Recomendado para Python)

#* CONCATENACIÓN CON +
name = 'Diego'
# Tenemos que tener en cuenta los espacios como un caracter más, no podemos usar un tipo de dato NO string en la variable
greeting = 'hi ' + name + ' how you doing?'
print(greeting)

#* CONCATENACIÓN CON F-STRINGS
# Esta sintaxis nos permite concatenar distintos tipos de datos, los convertirá a string (como las comillas francesas en JavaScript)
name = 5
greeting = f'hi {name} how you doing?'
print(greeting)

#* ELIMINAR VARIABLES (del)
nombre = 'Diego'
del nombre


#* OPERADORES DE PERTENENCIA (in / not in)
# Nos retorna una valor boolean en función de si lo encuentra o no. Es 'case sensitive'
string = 'hola buenas tardes'
print('ola' in string) #true
print('ola' not in string) #false



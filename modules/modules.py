# En python, se considera un módulo a cualquier archivo con la extensión .py
# Se les llama módulos porque pueden llamarse entre si
# Es una manera de separar un programa en partes para usarlo como nos convenga

# Existen 3 tipos de módulos

#? PYTHON MODULES
# Creados por python e incorporados por el propio lenguaje
# Están escritos en C (un lenguaje de más bajo nivel que python)

#? THIRD PARTY MODULES
# Módulos hechos por terceras personas, que nosotros podemos descargar y utilizar en nuestro código

#? OWN MODULES
# Módulos propios
# Son iguales que los third party, módulos creados por los usuarios


#* Importando el archivo greet_module
# Los inports se comportan como objetos, con sus métodos. Tambien llamados namespace
# En este caso la función greet del greet_module, se comportará como un método en este archivo
import greet_module as m # con 'as' podemos asignarle el nombre que queramos, como en JS
print(type(m)) # <class 'module'> 

saludo = m.greet('Lucas')
print(saludo) # hola Lucas, espero que hayas tenido un maravilloso día 

#* ver las propiedades y métodos del namespace
print(dir(m))
# [
  #! -- parte del objeto --
  # '__builtins__', 
  # '__cached__', 
  # '__doc__', 
  # '__file__', 
  # '__loader__', 
  # '__name__', 
  # '__package__', 
  # '__spec__', 
  #! -- Lo que creamos nosotros --
  #? 'greet', '
  #? greet_strange', 
  #? 'result'
# ]

#* Importando elementos concretos de un módulo. (funciones, clases, objetos, variables...)
# Podemos importar varias cosas a la vez y usar 'as'
from greet_module import greet as normal_greet, greet_strange

print(normal_greet('Diego')) # hola Diego, espero que hayas tenido un maravilloso día
print(greet_strange('Manu')) # Konda Manu! Espero que estes nashe, anasheli anashei
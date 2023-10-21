# Un paquete es una carpeta con varios modulos de python
import package

print(package.__path__) # ['c:\\cositas\\02-cursos\\05-python-Dalto\\modules\\package']  (ruta del paquete)

# Importando un modulo concreto del paquete
import package.greet_strange as m

print(m.greet_strange('Diego')) # Konda Diego! Espero que estes nashe, anasheli anashei  

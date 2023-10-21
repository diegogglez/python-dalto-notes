
#* Si el modulo esta en la misma carpeta se importa asi:
# import good_functions.greet as m

# print(m.greet('lucas'))

#* Si el múdulo está en un nivel anterior de carpeta:
import sys

sys.path.append('c:/cositas/02-cursos/05-python-Dalto/good_functions')

print(sys.path)
# Nos muestra rutas, la primera es la ruta actual, despues una lista con rutas de modulos instalados en python y 
# al final el modulo que introducimos en la lista con append()
# introducimos con el append

#? c:/cositas/02-cursos/05-python-Dalto/modules/modules_2.0.py <-- (Ruta actual)                                                                    
# [
  # 'c:\\cositas\\02-cursos\\05-python-Dalto\\modules', 
  # 'C:\\Python311\\python311.zip', 
  # 'C:\\Python311\\DLLs', 
  # 'C:\\Python311\\Lib', 
  # 'C:\\Python311', 
  # 'C:\\Python311\\Lib\\site-packages', 
  #* 'c:/cositas/02-cursos/05-python-Dalto/good_functions' <-- (Ruta introducida)
# ]  

import greet as m_greet

print(m_greet.greet('Diego')) # hola Diego, espero que hayas tenido un maravilloso día
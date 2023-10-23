
#* Con with open, el archivo se abre, se ejecuta el código del bloque, y se cierra
# El archivo por defecto se abre en modo lectura, podemos asignarle un nombre con as
# Este metodo es más óptimo, menos codigo y consume menos recursos
with open('files\\dalto_text.txt', encoding='UTF-8') as archivo:
  # leemos el archivo
  content = archivo.read()
  
  # mostramos el archivo
  print(content)
  
# El archivo se cierra automaticamente
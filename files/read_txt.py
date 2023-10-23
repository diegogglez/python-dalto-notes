
#* Usando open() para abrir un archivo con la codificación universal 'UTF-8'
archivo_sin_leer = open('files\\dalto_text.txt', encoding='UTF-8')

#* Usando la funcion read() para leer el archivo completo
# archivo = archivo_sin_leer.read()
# Tras leer un archivo es necesario cerrarlo para poder volver a leerlo más adelante


#* Usando readlines() para leer línea por línea
# Para archivos de texo grandes puede consumir toda la memoria del ordenador
# lines = archivo_sin_leer.readlines()
# print(lines) # ['si te está gustando el material, activa la campana.\n', 'Abogado, ¿Qué abogado?']  

#* Usando readline() para leer una sola línea
# como parámetro podemos pasar la cantidad de caracteres que queremos leer
line = archivo_sin_leer.readline()
print(line) # si te está gustando el material, activa la campana.  
#? en un texto plano, \n indica un salto de línea

#* cerrando el archivo
archivo_sin_leer.close()

# print(archivo_sin_leer.read()) #! ValueError: I/O operation on closed file.
# Una vez cerrado el archivo, si queremos volver a hacer operaciones de lectura, 
# necesitamos usar de nuevo open()

# Pero podemos usar los datos que ya tenemos guardados en una variable
print(line)
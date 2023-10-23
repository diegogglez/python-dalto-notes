
#* En este caso el segundo parámetro 'w' (write), indica que tenemos un permiso de escritura
with open('files\\dalto_text.txt', 'w', encoding='UTF-8') as archive:
  # Con write() sobreescribimos el archivo
  # archive.write('jajajja te la recontra teclee')
  
  # writelines() recibe como argumento una lista de lineas, lo inverso a readlines()
  # esta función no sobreescribe, concatena
  # con \n indicamos los saltos de linea
  #* Agredando 2 lineas
  archive.writelines(['- hola maestro, ¿cómo andas?\n', '- Misericordia\n'])
  #* Agregando otras 2 lineas
  archive.writelines(['- No se por qué dijiste eso\n', '- Yo tampoco\n'])
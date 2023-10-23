
#* En este caso el segundo parámetro 'a', indica append, a diferencia de 'w' (write) añade texto, pero no sobreescribe
# Los datos se agregan tantas veces como se ejecute este programa
with open('files\\dalto_text.txt', 'a', encoding='UTF-8') as archive:
  # agregando texto al archivo con un bucle for
  for i in range(5):
    archive.write(f'Linea {i + 1} agregada\n')
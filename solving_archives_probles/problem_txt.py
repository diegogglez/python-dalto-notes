# Tenemos dos listas, una con nombres y otra con apellidos
# Queremos registrar esta información en un archivo .txt de manera óptima

names = ['Lucas', 'Matias', 'Camila', 'Pedrp', 'Roberto']
lastnames = ['Dalto', 'Zing', 'Dalto', 'Robertix', 'Tarado']

with open('solving_archives_probles\\names_and_lastnames.txt', 'w') as archive:
  archive.writelines('Los datos son: \n\n')
  [archive.writelines(f'Nombre: {n}\nApellido: {l}\n------------\n') for n, l in zip(names, lastnames)]
  
# La sintaxis de la línea 9 hace lo mismo que:
# for n, l in zip(names, lastnames):
#   archive.writelines(f'Nombre: {n}\nApellido: {l}\n-----\n')
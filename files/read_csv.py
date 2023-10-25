import csv

with open('files\\data.csv') as data:
  reader = csv.reader(data)
  for row in reader:
    print(row)
    # ['nombre', ' "apellido"', ' "edad"']                                                                                                                                         
    # ['Lucas', ' "Dalto"', ' 99']                                                                                                                                                 
    # ['Roberto', ' "Demencial"', ' 42']                                                                                                                                           
    # ['Camila', ' "Dalto"', ' 24']
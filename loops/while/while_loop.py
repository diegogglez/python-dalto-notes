# A diferencia del bucle for, el bucle while se ejecuta mientras se cumpla una condición dada
# Esto significa que podríamos crear bucles infinitos

#* Ejemplo de bucle infinito:
# counter = 0
# while counter < 10:
#   print(counter)

#* Declarando un bucle que de 10 vueltas
counter = 0
while counter < 10:
  counter += 1
  print(counter)
  #? 1 (1 < 10 ? true)                                                                                                                                                                 
  #? 2 (2 < 10 ? true)                                                                                                                                                                       
  #? 3 (3 < 10 ? true) 
  #? 4 (4 < 10 ? true) 
  #? 5 (5 < 10 ? true) 
  #? 6 (6 < 10 ? true) 
  #? 7 (7 < 10 ? true) 
  #? 8 (8 < 10 ? true) 
  #? 9 (9 < 10 ? true) 
  #! 10 (10 < 10 ? false) --> La condición no se cumple, se termina el bucle.
  
print('El while llegó a su fin')
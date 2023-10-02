# ifs anidados y elif
# else if en Python se escribe: elif

ingreso_mensual = 12000
gasto_mensual = 5000

if ingreso_mensual > 10000:
  # print('Estás bien en cualquier parte del mundo')
  if ingreso_mensual - gasto_mensual < 0: # podemos anidar los ifs que queramos respetando la indentacion
    print('Estás en déficit')
  elif ingreso_mensual - gasto_mensual > 300:
    print('Bien pa, estás bien')
  else:
    print('Eh pa, estas gastando una banda, hay que ver si te alcanza')

elif ingreso_mensual > 1000:
  print('Estás bien en Latinoamerica')
  
elif ingreso_mensual > 500:
  print('Estás bien en Argentina')
  
elif ingreso_mensual > 200:
  print('Estás bien en Venezuela')

else:
  print('Sos pobre')
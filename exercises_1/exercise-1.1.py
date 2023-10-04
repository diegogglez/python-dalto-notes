# Promedio de duración
other_courses_min = 2.5
other_courses_max = 7
other_courses_Average = 4
dalto_course = 1.5

# Duración de crudos
average_raw = 5
dalto_raw = 3.5

# Diferencias de duración
diference_with_min = 100 - (dalto_course / other_courses_min * 100)
diference_with_max = 100 - (dalto_course * 1000 // other_courses_max / 10) 
# Añadimos ceros para borrar menos decimales y optener un resultado más preciso con la división //
diference_with_average = 100 - (dalto_course / other_courses_Average * 100)

# Calculando el porcentaje de tiempo vacío
average_empty_time = 100 - (other_courses_Average * 1000 // average_raw / 10) 
dalto_empty_time = 100 - (dalto_course * 1000 // dalto_raw / 10) 


# Mostrando las diferencias de duración (ejercicio A)
print('------------')
print('El curso de dalto dura:')
print(f'- Un {diference_with_min}% menos que el más rápido')
print(f'- Un {diference_with_max}% menos que el más lento')
print(f'- Un {diference_with_average}% menos que el promedio')
print('------------')

# Mostrando la cantidad de espacio que se elimina (ejercicio B)
print(f'Un curso promedio elimina un {average_empty_time}% de tiempo vacío')
print(f'Este curso eliminó un {dalto_empty_time}% de tiempo vacío')
print('------------')

# Mostrando diferencias si los cursos duraran 10h (ejercicio C)
print(f'Ver 10 horas de este curso equivale a ver {other_courses_Average * 100 // dalto_course / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_course * 100 // other_courses_Average / 10} horas de este curso')
print('------------')

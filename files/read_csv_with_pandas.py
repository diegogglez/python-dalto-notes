# pandas es una libreria de python para trabajar con analisis de datos
# Comunmente se importa con el nombre 'pd'
import pandas as pd

#* Usando la función read_csv para leer el archivo csv
# df hace referencia a 'Dataframe'. 
# Es una estructura de datos bidimensional similar a una hoja de cálculo
df = pd.read_csv('files\\data.csv')
df2 = pd.read_csv('files\\data.csv')

#* Obteniendo los datos de la columna 'nombre'
names = df['nombre']

#* Ordenando el dataframe por la edad
df_orden_descendente = df.sort_values('edad')
# print(df_orden_descendente)

#* Ordenandolo de forma descendente
df_orden_ascendente = df.sort_values('edad', ascending=False)
# print(df_orden_ascendente)

#* Concatenando los dos dataframes
df_concatenado = pd.concat([df, df2])
# print(df_concatenado)

#* accediendo a las primeras 3 filas con head()
# Como parámetro le pasamos el número de filas que queremos
primera_fila = df.head(3)
# print(primera_fila)

#* accediendo a las últimas 3 filas con tail()
ultimas_filas = df.tail(3)
# print(ultimas_filas)

#* accediendo a la cantidad de filas y columnas con shape
# devuelve una tupla con dos valores, el numero de filas y el número de columnas
# Podemos usar desempaquetado para guardar ambos valores en variables
filas_totales, columnas_totales = df.shape
# print(filas_totales, columnas_totales) # 5, 3

#* obteniendo estadisticas del dataframe
df_info = df.describe()
# print(df_info)

#* accediendo a un elemento específico del dataframe con loc
# accederemos a la edad de la fila 2
# le pasamos el índice de la fila y el nombre de la columna al que queremos acceder
item = df.loc[2, 'edad']
# print(item) # 24

#* accediendo a un elemento específico del dataframe con iloc
# accederemos a la edad de la fila 2
# podemos acceder al mismo valor usando solo índices de la fila y la columna
item = df.iloc[2, 2]
# print(item) # 24

#* accediendo a todas las filas de una columna
# con 'slicing' accedemos al apellido de todos los elementos
apellidos = df.iloc[:, 1]
# print(apellidos)

#* accediendo a todos los datos de la fila 3 con iloc
fila_3 = df.iloc[2, :]
print(fila_3)

#* accediendo a filas con edad > 30
mayor_de_30 = df.loc[df['edad'] > 30, :]
print(mayor_de_30)

# string = '0123456789'
# print(string[0:6]) 
# Esto se llama slicing, podemos indicar un rango de valores a tener en cuenta con ':' 
# En este caso imprimirá: 012345 
# si solo ponemos los : accederá a todos los elementos del iterable
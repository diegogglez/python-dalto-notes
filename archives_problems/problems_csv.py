# Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv('archives_problems\\data.csv')

#* Convertimos a string todos los datos de la columna 'edad'
df['edad'] = df['edad'].astype(str)

#* Mostrando el tipo de dato del primer elemento de la columna 'edad'
# print(type(df['edad'][0])) # <class 'str'>

#* Reemplazando los valores 'Dalto' por 'Maestro'
df['apellido'].replace('Dalto', 'Maestro', inplace=True)
# print(df)

#* Eliminando las filas con valores vacíos
# df = df.dropna(axis=1) --> para eliminar las columnas, por defecto es axis=0
df = df.dropna()
# print(df)

#* Eliminando filas repetidas
df = df.drop_duplicates()
# print(df)

#* Creando un CSV con el dataframe resultante
df.to_csv('archives_problems\\data_cleaned.csv')
import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archive_graphic_problems\\cofla_ingresos.csv')

#* Creando el gráfico
sns.barplot(x='fuente', y='ingresos', data=df)

#* Obteniendo el total de ingresos
total_ingresos = df['ingresos'].sum()

#* Mostrando el total de ingresos
print(f'El total de ingresos es de: {total_ingresos}€')

#* Mostrando el gráfico
plt.show()
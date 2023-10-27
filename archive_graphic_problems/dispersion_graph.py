import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archive_graphic_problems\\dispersion.csv')

#* Creando el gráfico
sns.scatterplot(x='tiempo', y='dinero', data=df)

#* Mostrando el gráfico
plt.show()
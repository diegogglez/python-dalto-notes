import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archive_graphic_problems\\bigotes.csv')

#* Creando el gráfico
sns.boxplot(x='categoria', y='valor', data=df)

#* Mostrando el gráfico
plt.show()
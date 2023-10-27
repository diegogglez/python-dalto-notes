import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archive_graphic_problems\\pedos.csv')

#* Creando el gráfico
sns.lineplot(x='fecha', y='pedos', data=df)

#* Creando un punto en el momento de más pedos
plt.plot('01-09', 17, 'o')

#* Mostrando el gráfico
plt.show()
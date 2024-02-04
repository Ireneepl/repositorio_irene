# PRÁCTICA WORKFLOW
# Archivo análisis dataset Titanic
# Irene Pico López

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
dataset_path = 'titanic_Workflow.csv'
df = pd.read_csv(dataset_path)

# Graficar los supervivientes por género
survived_by_gender = df.groupby(['survived', 'sex']).size().unstack()
survived_by_gender.plot(kind='bar', stacked=True)

# Personalizar el gráfico
plt.title('Nº de supervivientes en el Titanic por género')
plt.xlabel('Sobrevivió')
plt.ylabel('Cantidad')
plt.legend(title='Género', loc='upper right')
plt.xticks([0, 1], ['No', 'Sí'], rotation=0)

# Guardar la imagen
plt.savefig('grafico_titanic_por_genero.png')

# Mostrar el gráfico
plt.show()


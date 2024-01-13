
# Importando bibliotecas
import matplotlib.pyplot as plt
import pandas as pd

# Definindo DataFrame
gasolina_df = pd.read_csv('gasolina.csv', sep=',')

# Plotando um gráfico de barras usando Matplotlib
gasolina_df.plot(kind='line', x='dia', y='venda', legend=False)
plt.title('Preço da gasolina a cada dia')
plt.xlabel('Dia')
plt.ylabel('Preço')

# Salvando gráfico como png
plt.savefig('gasolina.png')

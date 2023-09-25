import pandas as pd
import matplotlib.pyplot as plt

# Criar um DataFrame de exemplo com dados de vendas
data = {
    'Data': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Produto A': [1000, 1200, 800, 1500, 1300, 1600, 1400, 1200, 1100, 1000, 900, 950],
    'Produto B': [800, 900, 750, 1300, 1100, 1400, 1200, 1100, 1000, 850, 800, 900],
}

df = pd.DataFrame(data)

# Configurar o índice para a coluna 'Data'
df.set_index('Data', inplace=True)

# Criar um gráfico de barras para visualizar as vendas de produtos
plt.figure(figsize=(10, 6))
ax = df.plot(kind='bar', stacked=False)
plt.title('Vendas de Produtos ao Longo do Tempo')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.legend(title='Produtos')

# Formatar o formato do mês na abscissa
ax.set_xticklabels([date.strftime('%b %Y') for date in df.index], rotation=45)

# Exibir o gráfico
plt.tight_layout()
plt.show()

import pandas as pd

# Carregar os dois arquivos Excel
arquivo1 = pd.read_excel('arquivo1.xlsx')
arquivo2 = pd.read_excel('arquivo2.xlsx')

# Comparar os dois DataFrames
diferencas = arquivo1.compare(arquivo2)

# Transpor o DataFrame de diferenças
diferencas = diferencas.transpose()

# Exibir as diferenças
print("Diferenças encontradas:")
print(diferencas)

# Exportar as diferenças para um arquivo Excel
diferencas.to_excel('diferencas.xlsx', index=True)

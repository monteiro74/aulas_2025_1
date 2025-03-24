# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p8_DBScan.py
#
# Descrição: Este script gera um gráfico de agrupamento usando o k-means,
#            e apresenta os dados na tela indicando o cluster de cada registro,
#            também permite que o valor de k seja ajustado.
#
# Autor: Nome do aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados e leitura do arquivo CSV.
# - matplotlib: Para exibir o gráfico.
# - KMeans: Para implementar o k-means.
# - sklearn: Biblioteca para aprendizado de máquina.
# - cluster: Usado para criar os cluster (agrupamentos) de dados.
# - StandardScaler: Para padronizar valores de variáveis.
#
# Uso: Rode este programa na mesma pasta com o arquivo clientes.csv
#      Altere o valor de k para ver os diferentes resultados
# ==============================================================================

# 1. Import
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 2. Carregar o arquivo CSV com delimitador ";"
#df = pd.read_csv('clientes.csv', sep=',')
df = pd.read_csv("clientes.csv", sep=";")

# 3. Verificar os nomes das colunas
print(df.columns)

# 4. Ajuste: usar os nomes corretos das colunas
X = df[['Idade', 'Renda']]  # Use exatamente como os nomes aparecem

# 5. Normalizar os dados (é importante para o DBSCAN)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 6. Aplicar o DBSCAN
db = DBSCAN(eps=0.5, min_samples=5)  # Ajuste os parâmetros conforme necessário
clusters = db.fit_predict(X_scaled)

# 7. Adicionar a coluna de clusters ao DataFrame
df['cluster'] = clusters

# 8. Exibir os resultados
print(df.head())

# 9. Plotar os resultados
plt.figure(figsize=(8,6))
plt.scatter(df['Idade'], df['Renda'], c=df['cluster'], cmap='viridis', s=50)
plt.title('Clustering dos Clientes com DBSCAN')
plt.xlabel('Idade')
plt.ylabel('Renda')
plt.colorbar(label='Cluster')
plt.show()


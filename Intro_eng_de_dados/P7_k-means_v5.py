# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p6_gerando_dados.py
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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Carregar o dataset
#df = pd.read_csv("clientes.csv")
df = pd.read_csv("clientes.csv", sep=";")

# 2. Selecionar as colunas "Idade" e "Renda" para aplicar o K-means
X = df[['Idade', 'Renda']]

# 3. Normalizar os dados (opcional, mas recomendado)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Definir o número de clusters (K)
k = 3  # Escolhendo K = 3 como exemplo

# 5. Executar o K-means
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X_scaled)

# 6. Adicionar os rótulos (clusters) ao DataFrame original
df['Cluster'] = kmeans.labels_

# 7. Visualizar os clusters (gráfico)
plt.figure(figsize=(8, 6))
plt.scatter(df['Idade'], df['Renda'], c=df['Cluster'], cmap='viridis', marker='o')
plt.title('Clusters de Clientes (K-means)')
plt.xlabel('Idade')
plt.ylabel('Renda')
plt.colorbar(label='Cluster')
plt.show()

# 8. Exibir o DataFrame com os clusters
print(df)

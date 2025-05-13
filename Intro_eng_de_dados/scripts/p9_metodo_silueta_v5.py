# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: metodo_silueta.py
#
# Descrição: Este script implementa o índice silueta, que é uma medida de quão 
# bem cada ponto de dados se ajusta ao seu cluster em comparação com outros clusters. 
# Ele varia de -1 a +1, onde valores mais altos indicam que os pontos estão bem agrupados.
#
# Autor: Nome do aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - matplotlig: Para exibir o gráfico.
# - KMeans: Para implementar o k-means.
# - silhouette_score: Esta função retorna o coeficiente de silhueta médio sobre 
#   todas as amostras.
#
# Uso: Rode este programa na mesma pasta com o arquivo clientes.csv
# ==============================================================================

# 1. Import
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 2. Carregando os dados fictícios
df = pd.read_csv("clientes.csv", sep=";")

# 3. Usando as colunas "Idade" e "Renda" para aplicar o K-means
X = df[['Idade', 'Renda']]

# 4. Testando diferentes valores de K (de 2 a 10)
silhouette_scores = []

for k in range(2, 11):  # Inicia de 2 pois o índice de silhueta não pode ser calculado para K=1
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    score = silhouette_score(X, kmeans.labels_)
    silhouette_scores.append(score)

# 5. Plotando o gráfico de Silhueta
plt.figure(figsize=(8, 6))
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Método Silhouette')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Índice de Silhueta')
plt.show()

# 6. Determinando o número de clusters recomendados
# O número de clusters recomendado é o valor de K com o maior índice de silhueta
numero_clusters_recomendado = range(2, 11)[np.argmax(silhouette_scores)]
print(f"Número de clusters recomendados: {numero_clusters_recomendado}")
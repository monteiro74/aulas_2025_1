# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: metodo_cotovelo.py
#
# Descrição: Este script envolve a execução do algoritmo K-means para diferentes 
# valores de K e depois calcular a soma das distâncias quadráticas dentro do 
# cluster (chamada de inércia). O gráfico gerado ajuda a identificar o "cotovelo", 
# que é onde a inércia começa a diminuir de forma menos acentuada. O valor de K 
# correspondente a esse ponto geralmente é o melhor número de clusters.
# Inércia (a soma das distâncias quadráticas entre os pontos e seus centros de cluster).
#
# Autor: Nome do aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados e leitura do arquivo CSV.
# - matplotlig: Para exibir o gráfico.
# - KMeans: Para implementar o k-means.
# - numpy: Lib para processamento de matriz/processamento matemático.
#
# Saída: Se o resultado é 2 então
#
# Uso: Rode este programa na mesma pasta com o arquivo clientes.csv
# ==============================================================================

# 1. Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 2. Carregando os dados fictícios criados anteriormente
# Especificando o delimitador ";" ao carregar o arquivo CSV
df = pd.read_csv("clientes.csv", sep=";")

# 3. Usando as colunas "Idade" e "Renda" para aplicar o K-means
X = df[['Idade', 'Renda']]

# 4. Inicializando uma lista para armazenar os valores da inércia
inercia = []

# 5. Testando diferentes valores de K (de 1 a 10)
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inercia.append(kmeans.inertia_)

# 6. Plotando o gráfico do Método do Cotovelo
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), inercia, marker='o')
plt.title('Método do Cotovelo')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Inércia')
plt.show()

# 7. Determinando o número de clusters recomendados
# Calculando a diferença entre os valores de inércia consecutivos
diferencas = np.diff(inercia)
# Calculando a diferença das diferenças para encontrar o "cotovelo"
diferencas_das_diferencas = np.diff(diferencas)
# O ponto de cotovelo é onde a segunda diferença é máxima
numero_clusters_recomendado = np.argmax(diferencas_das_diferencas) + 2  # +2 porque usamos diff duas vezes

print(f"Número de clusters recomendados: {numero_clusters_recomendado}")
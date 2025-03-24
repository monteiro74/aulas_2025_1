# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p10_classificacao_arvore.py
#
# Descrição: Este script gera uma tabela com um campo novo chamado classe prevista
#            e a saída é gravada em um arquivo csv e um gráfico de árvore de decisão 
#            ele implementa a classificação usando arvore de decisão.
#            Gera ao final o dataset: clientes_classificados3.csv
#
# Autor: Nome do aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados e leitura do arquivo CSV.
# - sklearn: Biblioteca para aprendizado de máquina.
#
# Uso: Rode este programa na mesma pasta com o arquivo clientes.csv
# ==============================================================================

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# 1. Ler o arquivo clientes.csv
df = pd.read_csv('clientes.csv', delimiter=';')

# Exibir as primeiras linhas do DataFrame
print("Dataset original:")
print(df.head())

# 2. Preparar os dados
# Criar uma variável alvo fictícia: "Potencial" (1) ou "Não Potencial" (0)
df['Potencial'] = (df['Renda'] > 5000).astype(int)  # Exemplo simples de classificação

# Definir features (X) e target (y)
X = df[['Idade', 'Renda']]  # Variáveis independentes
y = df['Potencial']         # Variável dependente (alvo)

# 3. Treinar o modelo de árvore de decisão
modelo = DecisionTreeClassifier(max_depth=3)  # Limitamos a profundidade para facilitar a visualização
modelo.fit(X, y)

# 4. Visualizar a árvore de decisão sem o índice de Gini
plt.figure(figsize=(12, 8))
plot_tree(
    modelo,
    filled=True,
    feature_names=['Idade', 'Renda'],
    class_names=['Não Potencial', 'Potencial'],
    impurity=False  # Isso remove o índice de Gini da visualização
)
plt.title("Árvore de Decisão para Classificação de Clientes")
plt.show()

# 5. Classificar os registros e adicionar uma nova coluna ao dataset
# Usar o modelo para prever a classificação de cada registro
df['Classificacao'] = modelo.predict(X)

# Mapear os valores 0 e 1 para "Não Potencial" e "Potencial"
df['Classificacao'] = df['Classificacao'].map({0: 'Não Potencial', 1: 'Potencial'})

# Exibir o dataset com a nova coluna de classificação
print("\nDataset com classificação:")
print(df)

# 6. Salvar o resultado em um novo arquivo CSV
df.to_csv('clientes_classificados3.csv', index=False, sep=';')
print("\nResultado salvo no arquivo 'clientes_classificados3.csv'.")
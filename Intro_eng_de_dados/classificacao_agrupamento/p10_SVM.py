# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: svm_classificacao_visual.py - Classificação com SVM
# Descrição:
#   Este script aplica o algoritmo SVM para classificar dados de um dataset CSV.
#   Ao final, gera um gráfico visual comparando a classe real com a prevista para
#   cada exemplo do conjunto de teste, facilitando o entendimento por parte dos alunos.
#
# Autor: Nome do aluno
# Data de Criação:
# Hora de Criação:
#
# Dependências:
# - pandas: para manipulação dos dados
# - scikit-learn: para modelo SVM e métricas
# - matplotlib: para geração de gráficos
# - time, datetime: para medir tempo de execução
#
# Uso: Coloque o arquivo 'dataset_para_classificacao_v2.csv' na mesma pasta do script.
# ==============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import time
import datetime

# Início
inicio = time.time()
print("Início do processamento:", datetime.datetime.now())

# Carregar o dataset
arquivo_csv = 'dataset_para_classificacao_v2.csv'
df = pd.read_csv(arquivo_csv, sep=';')

# Separar variáveis independentes (X) e dependente (y)
X = df[['idade', 'salario_anual', 'tempo_empresa', 'score_credito']]
y = df['classe']

# Padronizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

# Treinar modelo SVM
modelo = SVC()
modelo.fit(X_train, y_train)

# Realizar predições
y_pred = modelo.predict(X_test)

# Gerar relatório em CSV
report = classification_report(y_test, y_pred, output_dict=True)
df_report = pd.DataFrame(report).transpose()
df_report.to_csv("resultado_svm.csv", sep=';', index=True)

plt.figure(figsize=(12, 6))
largura = 0.4
indices = np.arange(len(y_test))

plt.bar(indices - largura/2, y_test, width=largura, label='Classe Real', color='skyblue')
plt.bar(indices + largura/2, y_pred, width=largura, label='Classe Prevista', color='salmon')

plt.title('Classificação por Amostra - SVM')
plt.xlabel('Índice da Amostra (conjunto de teste)')
plt.ylabel('Classe (0 ou 1)')
plt.xticks(indices)
plt.yticks([0, 1])
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("grafico_barras_classificacao_svm.png")
plt.close()

# Fim
fim = time.time()
print("Fim do processamento:", datetime.datetime.now())
print("Tempo total: {:.2f} segundos".format(fim - inicio))

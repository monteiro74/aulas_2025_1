# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p1.py - Estatística básica
# Descrição: Este script carrega um arquivo CSV (dataset1.csv), e 
#            realiza calculos estatísticos iniciais.
#
# Autor: Nome do aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados e leitura do arquivo CSV.
#
# Uso: Coloque o dataset1.csv na mesma pasta que este programa
# ==============================================================================

import pandas as pd
import numpy as np
import statistics as stats
from datetime import datetime

# Início do processamento
tempo_inicio = datetime.now()
print(f"Início do processamento: {tempo_inicio.strftime('%H:%M:%S')}")

# Leitura do arquivo CSV
df = pd.read_csv('dataset1.csv', sep=';', dtype={'Nome': str, 'Idade': float, 'Sexo': str})

# Remover linhas onde a idade está faltando
df_limpo = df.dropna(subset=['Idade'])

# Extração da coluna Idade
idades = df_limpo['Idade'].tolist()

# Cálculos
media = np.mean(idades)
mediana = np.median(idades)
moda = stats.mode(idades)
variancia = np.var(idades, ddof=1)  # ddof=1 para amostra
desvio_padrao = np.std(idades, ddof=1)

# Definir se o desvio padrão é alto ou baixo
limite = media * 0.2  # Considerando 20% da média como referência
if desvio_padrao > limite:
    classificacao_dp = "alto"
else:
    classificacao_dp = "baixo"

# Exibir resultados
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Variância: {variancia:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f} ({classificacao_dp})")

# Fim do processamento
tempo_fim = datetime.now()
print(f"Fim do processamento: {tempo_fim.strftime('%H:%M:%S')}")

# Tempo total
tempo_total = tempo_fim - tempo_inicio
print(f"Tempo total de processamento: {tempo_total}")

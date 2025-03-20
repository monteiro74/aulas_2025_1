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
# - numpy biblioteca científica.
# - statistics biblioteca estatística.
# - biblioteca para manipular datas e hora.
#
# Uso: Coloque o dataset1.csv na mesma pasta que este programa.
#
# Dados apresentados:
# - Média: soma de todos os valores dividida pelo número de elementos.
# - Mediana: valor central de um conjunto ordenado de dados.
# - Moda: valor que mais se repete em um conjunto de dados.
# - Variância: medida da dispersão dos dados em relação à média.
# - Amplitude: diferença entre o maior e o menor valor do conjunto.
# - Desvio padrão: Indicando a dispersão dos dados. O desvio padrão mede o quanto os 
#   valores de um conjunto de dados estão espalhados em relação à média. Desvio padrão 
#   baixo: os valores estão próximos da média. Desvio padrão alto: os valores estão 
#   mais dispersos, ou seja, há maior variação.
#
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

# Contagem de registros no dataset
registro_count = len(df)
print(f"Total de registros: {registro_count}")

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

# Idade máxima e mínima
idade_maxima = max(idades)
idade_minima = min(idades)

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
print(f"Idade Máxima: {idade_maxima}")
print(f"Idade Mínima: {idade_minima}")

# Exibir campos e tipos de dados
print("\nCampos e Tipos de Dados:")
print(df.dtypes)

# Fim do processamento
tempo_fim = datetime.now()
print(f"Fim do processamento: {tempo_fim.strftime('%H:%M:%S')}")

# Tempo total
tempo_total = tempo_fim - tempo_inicio
print(f"Tempo total de processamento: {tempo_total}")

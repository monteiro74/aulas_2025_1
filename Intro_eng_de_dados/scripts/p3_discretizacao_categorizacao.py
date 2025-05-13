# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p2.py - Exemplo de discretização e agrupamento
# Descrição: Este script carrega um arquivo CSV, e aplica a discretização
#            na coluna idade e apresenta um agrupamento por categoria "faixa etária"
#
# Autor: Nome do aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados e leitura do arquivo CSV.
# - numpy:  Usado para computação numérica
#
# Uso: Coloque o dataset na mesma pasta que este programa
# ==============================================================================

import pandas as pd
import numpy as np  

# Lendo o dataset a partir do arquivo CSV
df = pd.read_csv("dataset1.csv", sep=";")

# Removendo espaços extras dos nomes das colunas e convertendo para minúsculas
df.columns = df.columns.str.strip().str.lower()

# Definindo os intervalos e rótulos para discretização
bins = [0, 25, 40, np.inf]  # Faixas de idade
labels = ["Jovem", "Adulto", "Idoso"]

# Convertendo a coluna "idade" para numérica
df["idade"] = pd.to_numeric(df["idade"], errors="coerce")

# Aplicando a discretização na coluna "idade"
df["faixa_etaria"] = pd.cut(df["idade"], bins=bins, labels=labels)

# Contando a quantidade de registros por faixa etária
resultado = df["faixa_etaria"].value_counts().reset_index()
resultado.columns = ["faixa_etaria", "quantidade"]

# Exibindo o resultado
print(resultado)

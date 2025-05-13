# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p1.py - Contagem de Dados Faltantes no Dataset
# Descrição: Este script carrega um arquivo CSV, verifica e conta os valores
#            ausentes (faltantes) em cada coluna do dataset, e exibe a quantidade
#            de dados faltantes para cada coluna.
#
# Autor: Nome do aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados e leitura do arquivo CSV.
# - numpy biblioteca científica.
#
# Uso: Coloque o dataset na mesma pasta que este programa
# ==============================================================================

import pandas as pd
import numpy as np  

# Lendo o dataset a partir do arquivo CSV
df = pd.read_csv("dataset1.csv", sep=";")

# Exibir as primeiras linhas para verificar se a coluna "idade" existe
print("Colunas do dataset:", df.columns)  # Isso ajudará a ver os nomes exatos

# Remover espaços extras nos nomes das colunas (caso existam)
df.columns = df.columns.str.strip().str.lower()  # Converte para minúsculas

# Verificar se "idade" está presente
if "idade" not in df.columns:
    raise KeyError("A coluna 'idade' não foi encontrada no dataset. Verifique o nome correto.")

# Definindo os intervalos e rótulos para discretização
bins = [0, 25, 40, np.inf]  # Faixas de idade
labels = ["Jovem", "Adulto", "Idoso"]

# Convertendo a coluna "idade" para numérica
df["idade"] = pd.to_numeric(df["idade"], errors="coerce")

# Aplicando a discretização na coluna "idade"
df["faixa_etaria"] = pd.cut(df["idade"], bins=bins, labels=labels)

# Exibindo as primeiras linhas do DataFrame atualizado
#print(df.head())
print(df)

# Salvando o novo dataset com a coluna "faixa_etaria"
df.to_csv("dataset1_discretizado.csv", sep=";", index=False)
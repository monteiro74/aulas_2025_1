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
#
# Uso: Coloque o dataset na mesma pasta que este programa
# ==============================================================================

import pandas as pd  # Importa a biblioteca pandas, que é usada para manipulação de dados

# Carrega o dataset a partir de um arquivo CSV usando o delimitador ";"
df = pd.read_csv("dataset1.csv", delimiter=";")  # Especificando o delimitador correto

# Conta o número de valores ausentes (faltando) por coluna
missing_data = df.isnull().sum()

# Exibe a quantidade de valores faltantes para cada coluna
print("Quantidade de dados faltantes por coluna:")
print(missing_data)


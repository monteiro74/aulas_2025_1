# -----------------------------------------------------------
# Script: grafico_preco_casa_mysql.py
# Autor: ChatGPT - Especialista em Python e Ciência de Dados
# Descrição: Conecta-se a um banco MySQL, lê dados de casas
#            (tamanho, quartos, preço), aplica regressão linear
#            e gera gráfico com reta de regressão. Salva em PNG.
# Dependências: pandas, matplotlib, sklearn, mysql-connector-python
# Execução: python grafico_preco_casa_mysql.py
# -----------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import mysql.connector

# -------- CONFIGURAÇÕES DO BANCO DE DADOS --------
# Altere os dados de conexão abaixo conforme seu ambiente
conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="nome_do_banco"
)

# Consulta SQL
query = "SELECT tamanho, quartos, preco FROM casas"
df = pd.read_sql(query, conexao)

# Pré-processamento
X = df[['tamanho']]
y = df['preco']

# Modelo de regressão
modelo = LinearRegression()
modelo.fit(X, y)

# Geração da reta de regressão
tamanhos = np.linspace(X.min(), X.max(), 100)
precos = modelo.predict(tamanhos)

# Previsão específica (exemplo para 90 m²)
entrada = pd.DataFrame([[90]], columns=['tamanho'])
previsao = modelo.predict(entrada)

# Gráfico
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(tamanhos, precos, color='red', label='Reta de regressão')
plt.scatter(90, previsao, color='green', label=f'Previsão p/ 90m²: R$ {previsao[0]:,.0f}')
plt.title('Preço da Casa vs Tamanho (Regressão Linear)')
plt.xlabel('Tamanho (m²)')
plt.ylabel('Preço (R$)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_preco_casa_mysql.png")
plt.show()

conexao.close()

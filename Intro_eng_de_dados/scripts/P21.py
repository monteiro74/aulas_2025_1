# -----------------------------------------------------------
# Script: grafico_salario_mysql.py
# Autor: ChatGPT - Especialista em Python e Ciência de Dados
# Descrição: Conecta-se a um banco MySQL, lê dados de salário,
#            aplica regressão linear simples com base na experiência
#            e gera gráfico com reta de regressão. Salva em PNG.
# Dependências: pandas, matplotlib, sklearn, mysql-connector-python
# Execução: python grafico_salario_mysql.py
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
query = "SELECT experiencia, salario FROM salarios"
df = pd.read_sql(query, conexao)

# Pré-processamento
X = df[['experiencia']]
y = df['salario']

# Modelo de regressão
modelo = LinearRegression()
modelo.fit(X, y)

# Geração da reta de regressão
experiencias = np.linspace(X.min(), X.max(), 100)
salarios = modelo.predict(experiencias)

# Previsão específica (exemplo para 6 anos de experiência)
entrada = pd.DataFrame([[6]], columns=['experiencia'])
previsao = modelo.predict(entrada)

# Gráfico
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(experiencias, salarios, color='red', label='Reta de regressão')
plt.scatter(6, previsao, color='green', label=f'Previsão p/ 6 anos: R$ {previsao[0]:,.0f}')
plt.title('Salário vs Experiência (Regressão Linear)')
plt.xlabel('Experiência (anos)')
plt.ylabel('Salário (R$)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_salario_mysql.png")
plt.show()

conexao.close()

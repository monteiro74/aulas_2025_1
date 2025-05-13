# -----------------------------------------------------------
# Script: regressao_preco_casa_grafico.py
# Autor: ChatGPT - Especialista em Python e Ciência de Dados
# Descrição: Regressão linear simples para prever o preço
#            de casas com base no tamanho. Mostra gráfico
#            com pontos e reta de regressão. Salva gráfico em .PNG.
# Dependências: pandas, matplotlib, scikit-learn
# Execução: python regressao_preco_casa_grafico.py
# -----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Dados simulados
dados = pd.DataFrame({
    'tamanho': [70, 100, 120],
    'preco': [250000, 400000, 500000]
})

# X e y
X = dados[['tamanho']]
y = dados['preco']

# Treinamento
modelo = LinearRegression()
modelo.fit(X, y)

# Geração de pontos para reta
tamanhos_novos = np.linspace(X.min(), X.max(), 100)
precos_previstos = modelo.predict(tamanhos_novos)

# Previsão específica
entrada = pd.DataFrame([[90]], columns=['tamanho'])
previsao = modelo.predict(entrada)

# Gráfico
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(tamanhos_novos, precos_previstos, color='red', label='Reta de regressão')
plt.scatter(90, previsao, color='green', label=f'Previsão p/ 90m²: R$ {previsao[0]:,.0f}')
plt.title('Regressão Linear - Preço da Casa vs Tamanho')
plt.xlabel('Tamanho (m²)')
plt.ylabel('Preço (R$)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_preco_casa.png")
plt.show()

# -----------------------------------------------------------
# Script: regressao_salario_grafico.py
# Autor: ChatGPT - Especialista em Python e Ciência de Dados
# Descrição: Regressão linear simples para prever salário
#            com base na experiência. Mostra gráfico
#            com pontos e reta de regressão. Salva gráfico em .PNG.
# Dependências: pandas, matplotlib, scikit-learn
# Execução: python regressao_salario_grafico.py
# -----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Dados simulados (fixando escolaridade para visualização)
dados = pd.DataFrame({
    'experiencia': [1, 3, 5, 7, 10],
    'escolaridade': [0, 0, 1, 1, 1],  # 0 = Médio, 1 = Superior
    'salario': [1500, 2000, 3500, 4500, 6000]
})

# Foco em experiência para plotar 2D
X = dados[['experiencia']]
y = dados['salario']

modelo = LinearRegression()
modelo.fit(X, y)

# Geração da reta
experiencias_novas = np.linspace(X.min(), X.max(), 100)
salarios_previstos = modelo.predict(experiencias_novas)

# Previsão específica para 6 anos
entrada = pd.DataFrame([[6]], columns=['experiencia'])
previsao = modelo.predict(entrada)

# Gráfico
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(experiencias_novas, salarios_previstos, color='red', label='Reta de regressão')
plt.scatter(6, previsao, color='green', label=f'Previsão p/ 6 anos: R$ {previsao[0]:,.0f}')
plt.title('Regressão Linear - Salário vs Experiência')
plt.xlabel('Experiência (anos)')
plt.ylabel('Salário (R$)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_salario.png")
plt.show()

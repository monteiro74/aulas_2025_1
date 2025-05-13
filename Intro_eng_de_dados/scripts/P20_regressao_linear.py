# -----------------------------------------------------------
# Script: regressao_preco_casa.py
# Autor: ChatGPT - Especialista em Python e Ciência de Dados
# Descrição: Exemplo de regressão linear usando scikit-learn
#            para prever o preço de uma casa com base em
#            tamanho (m²) e número de quartos.
# Dependências: pandas, scikit-learn
# Execução: python regressao_preco_casa.py
# -----------------------------------------------------------

from sklearn.linear_model import LinearRegression
import pandas as pd

# Dados simulados
dados = pd.DataFrame({
    'tamanho': [70, 100, 120],
    'quartos': [2, 3, 4],
    'preco': [250000, 400000, 500000]
})

# Variáveis independentes (X) e dependente (y)
X = dados[['tamanho', 'quartos']]
y = dados['preco']

# Treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)

# Previsão para uma nova casa: 90m², 3 quartos
entrada = pd.DataFrame([[90, 3]], columns=['tamanho', 'quartos'])
previsao = modelo.predict(entrada)

print(f"Preço previsto para casa de 90m² e 3 quartos: R$ {previsao[0]:,.2f}")

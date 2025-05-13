# -----------------------------------------------------------
# Script: regressao_salario.py
# Autor: ChatGPT - Especialista em Python e Ciência de Dados
# Descrição: Exemplo de regressão linear usando scikit-learn
#            para prever salário com base em anos de experiência
#            e escolaridade (0 = Médio, 1 = Superior).
# Dependências: pandas, scikit-learn
# Execução: python regressao_salario.py
# -----------------------------------------------------------

from sklearn.linear_model import LinearRegression
import pandas as pd

# Dados simulados
dados = pd.DataFrame({
    'experiencia': [1, 3, 5, 7, 10],
    'escolaridade': [0, 0, 1, 1, 1],  # 0 = Médio, 1 = Superior
    'salario': [1500, 2000, 3500, 4500, 6000]
})

# Variáveis independentes (X) e dependente (y)
X = dados[['experiencia', 'escolaridade']]
y = dados['salario']

# Treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)

# Previsão para uma pessoa com 6 anos de experiência e ensino superior
entrada = pd.DataFrame([[6, 1]], columns=['experiencia', 'escolaridade'])
previsao = modelo.predict(entrada)

print(f"Salário previsto para 6 anos de experiência e superior: R$ {previsao[0]:,.2f}")
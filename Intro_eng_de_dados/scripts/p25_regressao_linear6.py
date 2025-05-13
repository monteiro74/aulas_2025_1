# -----------------------------------------------------------
# Script: regressao_altura_idade.py
# Autor: ChatGPT - Especialista em Python e Ciência de Dados
# Descrição: Gera dados fictícios de altura x idade, simula
#            crescimento de crianças ao longo dos anos e
#            aplica regressão linear simples. Salva gráfico .PNG.
# Dependências: pandas, matplotlib, numpy
# Execução: python regressao_altura_idade.py
# -----------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Gerar dados fictícios
np.random.seed(0)
idades = np.arange(2, 18)
alturas = 50 + idades * 6 + np.random.normal(0, 5, len(idades))
df = pd.DataFrame({'idade': idades, 'altura': alturas.round(1)})

# Salvar CSV
df.to_csv("dados_altura_idade.csv", index=False)

# Regressão linear com numpy
coef = np.polyfit(df['idade'], df['altura'], 1)
reta = np.poly1d(coef)

# Gerar gráfico
plt.figure(figsize=(8, 5))
plt.scatter(df['idade'], df['altura'], label='Dados reais', color='blue')
plt.plot(df['idade'], reta(df['idade']), color='red', label='Reta de regressão')
plt.title('Altura x Idade (crianças)')
plt.xlabel('Idade (anos)')
plt.ylabel('Altura (cm)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_altura_idade.png")
plt.show()

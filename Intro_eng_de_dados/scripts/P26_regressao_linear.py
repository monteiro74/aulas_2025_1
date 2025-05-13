# -----------------------------------------------------------
# Script: regressao_nota_estudo.py
# Autor: ChatGPT - Especialista em Python e Ciência de Dados
# Descrição: Gera dados fictícios de horas de estudo e notas,
#            aplica regressão linear simples e visualiza em gráfico.
# Dependências: pandas, matplotlib, numpy
# Execução: python regressao_nota_estudo.py
# -----------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Gerar dados fictícios
np.random.seed(42)
horas_estudo = np.random.randint(0, 15, 50)
notas = 2 + 0.5 * horas_estudo + np.random.normal(0, 1, 50)
notas = np.clip(notas, 0, 10)
df = pd.DataFrame({'horas_estudo': horas_estudo, 'nota': notas.round(2)})

# Salvar CSV
df.to_csv("dados_nota_estudo.csv", index=False)

# Regressão linear com numpy
coef = np.polyfit(df['horas_estudo'], df['nota'], 1)
reta = np.poly1d(coef)

# Gerar gráfico
plt.figure(figsize=(8, 5))
plt.scatter(df['horas_estudo'], df['nota'], label='Dados reais', color='purple')
plt.plot(df['horas_estudo'], reta(df['horas_estudo']), color='orange', label='Reta de regressão')
plt.title('Nota Final x Horas de Estudo')
plt.xlabel('Horas de estudo por semana')
plt.ylabel('Nota final')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_nota_estudo.png")
plt.show()

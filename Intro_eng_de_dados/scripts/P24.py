# -----------------------------------------------------------
# Script: regressao_sorvete_temperatura.py
# Autor: ChatGPT - Especialista em Python e Ciência de Dados
# Descrição: Gera dados fictícios de temperatura e vendas de sorvete,
#            aplica regressão linear e visualiza gráfico com PNG.
# Dependências: pandas, matplotlib, numpy
# Execução: python regressao_sorvete_temperatura.py
# -----------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Gerar dados fictícios
np.random.seed(10)
temperaturas = np.linspace(20, 40, 50)
vendas = 100 + (temperaturas - 20) * 15 + np.random.normal(0, 10, 50)
df = pd.DataFrame({'temperatura': temperaturas.round(1), 'vendas': vendas.round(0).astype(int)})

# Salvar CSV
df.to_csv("dados_sorvete_temperatura.csv", index=False)

# Regressão linear com numpy
coef = np.polyfit(df['temperatura'], df['vendas'], 1)
reta = np.poly1d(coef)

# Gerar gráfico
plt.figure(figsize=(8, 5))
plt.scatter(df['temperatura'], df['vendas'], label='Dados reais', color='green')
plt.plot(df['temperatura'], reta(df['temperatura']), color='red', label='Reta de regressão')
plt.title('Temperatura x Vendas de Sorvete')
plt.xlabel('Temperatura média (°C)')
plt.ylabel('Vendas diárias (unidades)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_sorvete_temperatura.png")
plt.show()

# -----------------------------------------------------------
# Script: segmentacao_kmeans.py
# Autor: ChatGPT - Especialista em Python e Ciência de Dados
# Descrição: Gera dados fictícios sobre experiência, escolaridade
#            e salário de profissionais. Aplica o algoritmo
#            não supervisionado K-Means para identificar grupos
#            de perfis semelhantes (segmentação de mercado).
#            Salva o gráfico em formato PNG.
# Dependências: pandas, numpy, sklearn, matplotlib
# Execução: python segmentacao_kmeans.py
# -----------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# --------- Gerar dados fictícios (simulação de uma base real) ---------
np.random.seed(42)  # Garantir repetibilidade
experiencia = np.random.randint(0, 30, 100)  # anos de experiência (0 a 29)
escolaridade = np.random.choice([0, 1, 2], 100)  # 0 = Fund., 1 = Médio, 2 = Superior
salario = experiencia * 400 + escolaridade * 2000 + np.random.normal(3000, 1500, 100)

# Criar DataFrame com os dados simulados
df = pd.DataFrame({
    'experiencia': experiencia,
    'escolaridade': escolaridade,
    'salario': salario.astype(int)
})

# --------- Aplicar o algoritmo K-Means ---------
# Defina abaixo o número de clusters desejado (valor de K)
# O aluno pode alterar o valor de K para explorar diferentes segmentações
k = 3  # <--- TROCAR AQUI: experimente usar k=2, k=4, k=5 e comparar os grupos
kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)

# Aplicar o modelo de agrupamento aos dados
df['grupo'] = kmeans.fit_predict(df[['experiencia', 'escolaridade', 'salario']])

# --------- Gerar gráfico de dispersão ---------
# Mostra a relação entre experiência e salário, colorindo por grupo
plt.figure(figsize=(8, 6))
cores = ['red', 'blue', 'green', 'purple', 'orange', 'cyan', 'gray']

for grupo in df['grupo'].unique():
    grupo_df = df[df['grupo'] == grupo]
    plt.scatter(grupo_df['experiencia'], grupo_df['salario'],
                color=cores[grupo % len(cores)],
                label=f'Grupo {grupo}', alpha=0.7)

plt.xlabel("Experiência (anos)")
plt.ylabel("Salário (R$)")
plt.title(f"Segmentação de Mercado com K-Means (k = {k})")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("segmentacao_kmeans.png")
plt.show()

# --------- Salvar os dados com rótulo de grupo ---------
df.to_csv("dados_segmentacao_kmeans.csv", index=False)


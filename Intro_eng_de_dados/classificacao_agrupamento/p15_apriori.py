# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: apriori_analysis.py - Análise de Conjuntos Frequentes com Gráficos
# Descrição: Este script aplica o Apriori no dataset 'dataset_conjunto_frequentes.csv',
#            exibe os 10 produtos mais frequentes, os 10 vendedores principais, e
#            gera gráficos salvos em PNG sobre produtos e regras de associação.
#
# Autor: Nome do aluno
# Data de Criação: 2025-04-23
# Hora de Criação: 14:00
#
# Dependências:
# - pandas, matplotlib, seaborn, mlxtend
#
# Uso: Coloque o arquivo 'dataset_conjunto_frequentes.csv' na mesma pasta.
# ==============================================================================

import pandas as pd
import time
from datetime import datetime
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Início do tempo
hora_inicio = datetime.now()
start_time = time.time()
print(f"Hora de início: {hora_inicio}")

# Leitura do dataset
df = pd.read_csv("dataset_conjunto_frequentes.csv", sep=';')

# Agrupar por comprador + data para formar transações
df['data_venda'] = pd.to_datetime(df['data_venda'])
df['transacao'] = df['comprador'] + "_" + df['data_venda'].dt.strftime('%Y-%m-%d')
transacoes = df.groupby('transacao')['descricao_produto'].apply(list).tolist()

# Codificar os dados para Apriori
te = TransactionEncoder()
te_ary = te.fit(transacoes).transform(transacoes)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Aplicar Apriori
frequent_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

# Top 10 produtos únicos
top_produtos = frequent_itemsets[frequent_itemsets['length'] == 1].nlargest(10, 'support')
top_produtos['produto'] = top_produtos['itemsets'].apply(lambda x: list(x)[0])

# Gráfico de produtos mais frequentes
plt.figure(figsize=(10, 6))
sns.barplot(data=top_produtos, x='support', y='produto', palette='viridis')
plt.title('Top 10 Produtos Mais Frequentes')
plt.xlabel('Suporte')
plt.ylabel('Produto')
plt.tight_layout()
plt.savefig("grafico_top10_produtos.png")
plt.close()

# Regras de associação com 2 itens
regras = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
regras_2itens = regras[regras['antecedents'].apply(lambda x: len(x) == 1) &
                       regras['consequents'].apply(lambda x: len(x) == 1)]

# 🔧 CORREÇÃO do erro de tipo em 'lift'
regras_2itens['lift'] = pd.to_numeric(regras_2itens['lift'], errors='coerce')
top_regras = regras_2itens.nlargest(10, 'lift')

# Preparar pares para gráfico
top_regras['antecedent'] = top_regras['antecedents'].apply(lambda x: list(x)[0])
top_regras['consequent'] = top_regras['consequents'].apply(lambda x: list(x)[0])
top_regras['par'] = top_regras['antecedent'] + ' → ' + top_regras['consequent']

# Gráfico de pares mais frequentes
plt.figure(figsize=(10, 6))
sns.barplot(data=top_regras, x='lift', y='par', palette='mako')
plt.title('Top 10 Produtos Comprados em Conjunto (Lift)')
plt.xlabel('Lift')
plt.ylabel('Produto A → Produto B')
plt.tight_layout()
plt.savefig("grafico_top10_regras.png")
plt.close()

# Top 10 vendedores dos produtos frequentes
produtos_top10 = top_produtos['produto'].tolist()
df_frequente = df[df['descricao_produto'].isin(produtos_top10)]
top_vendedores = df_frequente['vendedor'].value_counts().head(10).reset_index()
top_vendedores.columns = ['vendedor', 'quantidade_vendida']

# Exibir resumo
print("\nTop 10 produtos comprados com frequência:")
print(top_produtos[['produto', 'support']])

print("\nTop 10 vendedores dos produtos frequentes:")
print(top_vendedores)

print("\nTop 10 regras de associação entre produtos:")
print(top_regras[['par', 'support', 'confidence', 'lift']])

# Salvar CSVs
top_produtos.to_csv("top10_produtos_frequentes.csv", index=False)
top_vendedores.to_csv("top10_vendedores.csv", index=False)
top_regras[['par', 'support', 'confidence', 'lift']].to_csv("top10_regras_associacao.csv", index=False)

# Finalização do tempo
hora_fim = datetime.now()
tempo_total = hora_fim - hora_inicio
print(f"\nHora de término: {hora_fim}")
print(f"Tempo total de processamento: {tempo_total}")

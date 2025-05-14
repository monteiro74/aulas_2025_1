""# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: analise_bibliometrica.py - Análise Bibliométrica de Palavras-chave
# Descrição: Este script realiza a leitura de um arquivo RIS contendo artigos científicos,
#            gera gráficos de barras das palavras-chave mais frequentes e um mapa de 
#            coocorrência das palavras-chave. No final, exibe a quantidade total de artigos lidos.
#
# Autor: Nome do Aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados
# - matplotlib: Para plotar gráficos
# - seaborn: Para estilização dos gráficos
# - networkx: Para construção do grafo de coocorrência
#
# Uso: Coloque o arquivo RIS na mesma pasta que este programa
# ==============================================================================

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import networkx as nx
import seaborn as sns

# Caminho do arquivo RIS
file_path = 'dataset_artigos.ris'

# Função para extrair palavras-chave do arquivo RIS
def extract_keywords(file_path):
    keywords = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('KW  -'):
                keyword = line.replace('KW  - ', '').strip()
                keywords.append(keyword)
    return keywords

# Função para gerar o gráfico de barras das palavras-chave
def generate_bar_chart(keywords_list):
    keywords_counter = Counter(keywords_list)
    keywords_df = pd.DataFrame(keywords_counter.items(), columns=['Keyword', 'Frequency'])
    keywords_df = keywords_df.sort_values(by='Frequency', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Frequency', y='Keyword', data=keywords_df.head(20), palette='viridis')
    plt.title('Top 20 Palavras-chave')
    plt.savefig('grafico_barras_palavras_chave.png')
    plt.close()
    print("Gráfico de barras gerado: grafico_barras_palavras_chave.png")

# Função para gerar o mapa de coocorrência das palavras-chave
def generate_cooccurrence_map(keywords_list):
    coocurrence_pairs = []
    for keywords in keywords_list:
        split_keywords = keywords.split(', ')
        for i in range(len(split_keywords)):
            for j in range(i + 1, len(split_keywords)):
                coocurrence_pairs.append((split_keywords[i], split_keywords[j]))

    coocurrence_counter = Counter(coocurrence_pairs)
    coocurrence_df = pd.DataFrame(coocurrence_counter.items(), columns=['Pair', 'Frequency'])
    coocurrence_df[['Word1', 'Word2']] = pd.DataFrame(coocurrence_df['Pair'].tolist(), index=coocurrence_df.index)
    coocurrence_df = coocurrence_df.drop(columns=['Pair'])

    G = nx.Graph()
    for _, row in coocurrence_df.iterrows():
        G.add_edge(row['Word1'], row['Word2'], weight=row['Frequency'])

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    weights = [G[u][v]['weight'] for u, v in G.edges()]
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', edge_color=weights, width=2.0, edge_cmap=plt.cm.Blues)
    plt.title('Mapa de Coocorrência de Palavras')
    plt.savefig('mapa_coocorrencia_palavras.png')
    plt.close()
    print("Mapa de coocorrência gerado: mapa_coocorrencia_palavras.png")

# Função principal que executa as operações
def main():
    keywords_list = extract_keywords(file_path)
    print(f"Total de artigos lidos: {len(keywords_list)}")
    
    generate_bar_chart(keywords_list)
    generate_cooccurrence_map(keywords_list)

if __name__ == '__main__':
    main()
""

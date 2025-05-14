# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: analise_bibliometrica.py - Análise Bibliométrica de Artigos Científicos
# Descrição: Este script realiza a leitura de um arquivo RIS contendo artigos científicos,
#            gera gráficos de timeline de publicações, grafo de colaboração entre autores e 
#            dispersão de citações por ano. No final, exibe a quantidade total de artigos lidos.
#
# Autor: Nome do Aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados
# - matplotlib: Para plotar gráficos
# - seaborn: Para estilização dos gráficos
# - networkx: Para construção do grafo de colaboração
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

# Função para extrair informações do arquivo RIS
def extract_data(file_path):
    anos = []
    autores = []
    citacoes = []
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('PY  -'):
                ano = line.replace('PY  - ', '').strip()
                anos.append(ano)
            elif line.startswith('AU  -'):
                autor = line.replace('AU  - ', '').strip()
                autores.append(autor)
            elif line.startswith('N1  -'):
                citacao = line.replace('N1  - ', '').strip()
                if citacao.isdigit():
                    citacoes.append(int(citacao))

    return anos, autores, citacoes

# Função para gerar a Timeline de publicações
def generate_timeline(anos):
    anos_contagem = Counter(anos)
    anos_df = pd.DataFrame(anos_contagem.items(), columns=['Ano', 'Publicações'])
    anos_df = anos_df.sort_values(by='Ano')
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Ano', y='Publicações', data=anos_df, marker='o')
    plt.title('Timeline de Publicações')
    plt.savefig('timeline_publicacoes.png')
    plt.close()
    print("Timeline de publicações gerada: timeline_publicacoes.png")

# Função para gerar o grafo de colaboração entre autores
def generate_author_collaboration(autores):
    G = nx.Graph()
    for i in range(len(autores) - 1):
        G.add_edge(autores[i], autores[i + 1])
    
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', edge_color='gray')
    plt.title('Grafo de Colaboração entre Autores')
    plt.savefig('grafo_colaboracao_autores.png')
    plt.close()
    print("Grafo de colaboração gerado: grafo_colaboracao_autores.png")

# Função para gerar dispersão de citações por ano
def generate_citation_scatter(anos, citacoes):
    if len(anos) == len(citacoes):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=anos, y=citacoes)
        plt.title('Dispersão de Citações por Ano')
        plt.savefig('dispersao_citacoes_ano.png')
        plt.close()
        print("Dispersão de citações gerada: dispersao_citacoes_ano.png")
    else:
        print("Inconsistência nos dados de anos e citações.")

# Função principal que executa as operações
def main():
    anos, autores, citacoes = extract_data(file_path)
    print(f"Total de artigos lidos: {len(anos)}")
    
    generate_timeline(anos)
    generate_author_collaboration(autores)
    generate_citation_scatter(anos, citacoes)

if __name__ == '__main__':
    main()

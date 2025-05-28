# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p31.py - Análise de Interações sobre Eleições Americanas 2024
# Descrição: Este script simula interações no Twitter entre usuários políticos e mídias, constrói um grafo direcionado e calcula centralidade para exibir um mapa de rede.
#
# Autor: Nome do Aluno
# Data de Criação: 28/05/2025
# Hora de Criação: 22:37:03
#
# Dependências:
- networkx: Para construção do grafo
- matplotlib: Para visualização do grafo
#
# Uso: Execute diretamente para visualizar a rede simulada de interações.
# ==============================================================================

import networkx as nx
import matplotlib.pyplot as plt

# Simulando um dataset com interações no Twitter
interacoes = [
    ('@JoeBiden', '@KamalaHarris'),  # Biden mencionou Kamala
    ('@CNN', '@JoeBiden'),           # CNN retweetou Biden
    ('@elonmusk', '@realDonaldTrump'),
    ('@realDonaldTrump', '@elonmusk'),
    ('@nytimes', '@JoeBiden'),
    ('@user1', '@realDonaldTrump'),
    ('@user2', '@JoeBiden'),
    ('@user3', '@realDonaldTrump'),
    ('@user4', '@JoeBiden'),
    ('@user5', '@KamalaHarris'),
    ('@user6', '@elonmusk'),
    ('@KamalaHarris', '@JoeBiden')
]

# Criar grafo direcionado
G = nx.DiGraph()
G.add_edges_from(interacoes)

# Calcular métricas (ex: grau de entrada)
centralidade = nx.in_degree_centrality(G)

# Layout do grafo
pos = nx.spring_layout(G, k=0.5, seed=42)

# Tamanho dos nós baseado na centralidade
node_sizes = [1000 * centralidade.get(node, 0.1) for node in G.nodes()]

# Desenhar grafo
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue')
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
plt.title("Mapa de Rede - Interações sobre Eleições Americanas 2024")
plt.axis('off')
plt.tight_layout()
plt.show()

# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p33.py - Simulação de Rede Social com Centralidade
# Descrição: Este script cria uma rede social simulada e calcula a centralidade de entrada para destacar os usuários mais mencionados em um grafo.
#
# Autor: Nome do Aluno
# Data de Criação: 28/05/2025
# Hora de Criação: 22:37:03
#
# Dependências:
- networkx: Para criação da rede
- matplotlib: Para exibição gráfica
#
# Uso: Execute o script para ver um exemplo visual de rede social com centralidade.
# ==============================================================================


import networkx as nx
import matplotlib.pyplot as plt

# Criando uma rede social simulada
interacoes = [
    ('Ana', 'Bruno'),   # Ana menciona Bruno
    ('Bruno', 'Carlos'),
    ('Carlos', 'Ana'),
    ('Ana', 'Diana'),
    ('Diana', 'Carlos'),
    ('Eduardo', 'Bruno'),
    ('Eduardo', 'Diana'),
    ('Carlos', 'Bruno'),
    ('Fátima', 'Carlos'),
    ('Fátima', 'Ana')
]

# Criando o grafo
G = nx.DiGraph()  # DiGraph = grafo direcionado
G.add_edges_from(interacoes)

# Calcular centralidade de entrada (quem é mais mencionado)
centralidade = nx.in_degree_centrality(G)

# Layout
pos = nx.spring_layout(G, seed=42)
node_sizes = [8000 * centralidade.get(node, 0.01) for node in G.nodes()]

# Desenhar grafo
plt.figure(figsize=(10, 7))
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue')
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=12)

plt.title("Exemplo de Rede Social Simulada (Interações)")
plt.axis('off')
plt.tight_layout()
plt.show()


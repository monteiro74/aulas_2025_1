# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p32.py - Análise de Clusters e Tipos de Interação em Redes
# Descrição: Este script simula uma rede com dois clusters de usuários e um bot, além de mostrar uma segunda rede com tipos de interações rotuladas (menção, curtida, retweet).
#
# Autor: Nome do Aluno
# Data de Criação: 28/05/2025
# Hora de Criação: 22:37:03
#
# Dependências:
- networkx: Para construção dos grafos
- matplotlib: Para visualização
#
# Uso: Execute diretamente para ver duas visualizações de redes sociais.
# ==============================================================================


import networkx as nx
import matplotlib.pyplot as plt

# 1. Simulação com clusters e um "bot"
usuarios = {
    "Cluster A": ["Ana", "Bruno", "Carlos", "Diana"],
    "Cluster B": ["Eduardo", "Fátima", "Gabriel", "Helena"],
    "Bot": ["NewsBot"]
}

interacoes = [
    # Cluster A
    ("Ana", "Bruno"), ("Bruno", "Carlos"), ("Carlos", "Diana"), ("Diana", "Ana"),
    # Cluster B
    ("Eduardo", "Fátima"), ("Fátima", "Gabriel"), ("Gabriel", "Helena"), ("Helena", "Eduardo"),
    # Interações cruzadas
    ("Ana", "Fátima"), ("Carlos", "Gabriel"),
    # Bot interagindo com todos
    ("NewsBot", "Ana"), ("NewsBot", "Eduardo"), ("NewsBot", "Carlos"), ("NewsBot", "Gabriel")
]

G = nx.DiGraph()
G.add_edges_from(interacoes)

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)

# Destacar bot
colors = ["red" if n == "NewsBot" else "skyblue" for n in G.nodes()]
sizes = [1500 if n == "NewsBot" else 1000 for n in G.nodes()]

nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=sizes)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15)
nx.draw_networkx_labels(G, pos, font_size=10)
plt.title("Rede com Clusters e um Bot (NewsBot)")
plt.axis('off')
plt.tight_layout()
plt.show()

# 2. Rede com diferentes tipos de interação (pesos e rótulos)
G2 = nx.DiGraph()
interacoes_com_pesos = [
    ("Ana", "Bruno", "menção"),
    ("Bruno", "Carlos", "retweet"),
    ("Carlos", "Diana", "curtida"),
    ("Diana", "Ana", "menção"),
    ("Ana", "Carlos", "curtida"),
    ("NewsBot", "Ana", "retweet"),
    ("NewsBot", "Bruno", "menção"),
]

# Adiciona com rótulo como atributo
for origem, destino, tipo in interacoes_com_pesos:
    G2.add_edge(origem, destino, tipo=tipo)

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G2, seed=50)
nx.draw_networkx_nodes(G2, pos, node_color='lightgreen', node_size=1200)
nx.draw_networkx_edges(G2, pos, arrowstyle='->', arrowsize=15)
nx.draw_networkx_labels(G2, pos, font_size=10)

# Adiciona rótulos nas arestas com o tipo de interação
edge_labels = nx.get_edge_attributes(G2, 'tipo')
nx.draw_networkx_edge_labels(G2, pos, edge_labels=edge_labels, font_color='blue')

plt.title("Rede com Tipos de Interação (Menção, Curtida, Retweet)")
plt.axis('off')
plt.tight_layout()
plt.show()

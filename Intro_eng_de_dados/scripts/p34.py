# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p34.py - Árvore Genealógica com Relações Pai/Mãe → Filho
# Descrição: Este script constrói uma árvore genealógica com dados fictícios de uma família, diferenciando os gêneros e desenhando a rede com NetworkX.
#
# Autor: Nome do Aluno
# Data de Criação: 28/05/2025
# Hora de Criação: 22:37:03
#
# Dependências:
- pandas: Para manipulação de dados
- networkx: Para criar a árvore
- matplotlib: Para desenhar o grafo
#
# Uso: Execute para gerar e visualizar o grafo genealógico salvo em PNG.
# ==============================================================================

# -*- coding: utf-8 -*-
"""
Created on Wed May 28 18:27:48 2025

@author: usuario
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Lista de indivíduos com ID, nome, pai_id, mae_id e gênero
familia = [
    {"id": 1, "nome": "João", "pai_id": None, "mae_id": None, "genero": "M"},
    {"id": 2, "nome": "Maria", "pai_id": None, "mae_id": None, "genero": "F"},
    {"id": 3, "nome": "José", "pai_id": None, "mae_id": None, "genero": "M"},
    {"id": 4, "nome": "Ana", "pai_id": None, "mae_id": None, "genero": "F"},

    {"id": 5, "nome": "Carlos", "pai_id": 1, "mae_id": 2, "genero": "M"},
    {"id": 6, "nome": "Lucia", "pai_id": 1, "mae_id": 2, "genero": "F"},
    {"id": 7, "nome": "Marcos", "pai_id": 3, "mae_id": 4, "genero": "M"},
    {"id": 8, "nome": "Renata", "pai_id": 3, "mae_id": 4, "genero": "F"},

    {"id": 9, "nome": "Tiago", "pai_id": 5, "mae_id": 6, "genero": "M"},
    {"id": 10, "nome": "Camila", "pai_id": 5, "mae_id": 6, "genero": "F"},
    {"id": 11, "nome": "Lucas", "pai_id": 7, "mae_id": 8, "genero": "M"},
    {"id": 12, "nome": "Marina", "pai_id": 7, "mae_id": 8, "genero": "F"},
]

# Criar grafo dirigido
G = nx.DiGraph()

# Adicionar nós e arestas de parentesco
for pessoa in familia:
    G.add_node(pessoa["id"], label=pessoa["nome"], genero=pessoa["genero"])
    if pessoa["pai_id"]:
        G.add_edge(pessoa["pai_id"], pessoa["id"])
    if pessoa["mae_id"]:
        G.add_edge(pessoa["mae_id"], pessoa["id"])

# Cores por gênero
node_colors = []
for _, data in G.nodes(data=True):
    if data["genero"] == "M":
        node_colors.append("lightblue")
    elif data["genero"] == "F":
        node_colors.append("lightpink")
    else:
        node_colors.append("gray")

# Layout e plotagem
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42)
labels = {node: data["label"] for node, data in G.nodes(data=True)}

nx.draw(G, pos, labels=labels, with_labels=True,
        node_color=node_colors, node_size=1000, arrows=True, edge_color="gray")

plt.title("Árvore Genealógica com Gênero e Relações Pai/Mãe → Filho")
plt.axis("off")
plt.tight_layout()
plt.savefig("grafo_genealogico_genero.png")
plt.show()
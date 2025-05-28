# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p35.py - Árvore Genealógica Hierárquica com Gerações
# Descrição: Este script usa anytree e graphviz para gerar uma árvore genealógica com destaque por geração, colorida e com hierarquia vertical.
#
# Autor: Nome do Aluno
# Data de Criação: 28/05/2025
# Hora de Criação: 22:37:03
#
# Dependências:
- anytree: Para estrutura da árvore
- graphviz: Para renderização do grafo
#
# Uso: Execute o script para gerar e salvar uma árvore genealógica em PNG.
# ==============================================================================

# -*- coding: utf-8 -*-
"""
Created on Wed May 28 18:31:42 2025

@author: usuario
"""

from anytree import Node
from anytree.exporter import DotExporter
from graphviz import Source

# Lista de pessoas com pai_id e mae_id
familia_estendida = [
    {"id": 1, "nome": "João", "pai_id": None, "mae_id": None, "genero": "M"},
    {"id": 2, "nome": "Maria", "pai_id": None, "mae_id": None, "genero": "F"},
    {"id": 3, "nome": "José", "pai_id": None, "mae_id": None, "genero": "M"},
    {"id": 4, "nome": "Ana", "pai_id": None, "mae_id": None, "genero": "F"},
    {"id": 5, "nome": "Carlos", "pai_id": 1, "mae_id": 2, "genero": "M"},
    {"id": 6, "nome": "Lucia", "pai_id": 1, "mae_id": 2, "genero": "F"},
    {"id": 7, "nome": "Marcos", "pai_id": 3, "mae_id": 4, "genero": "M"},
    {"id": 8, "nome": "Renata", "pai_id": 3, "mae_id": 4, "genero": "F"},
    {"id": 9, "nome": "Paulo", "pai_id": 1, "mae_id": 2, "genero": "M"},
    {"id": 10, "nome": "Sandra", "pai_id": 3, "mae_id": 4, "genero": "F"},
    {"id": 11, "nome": "Tiago", "pai_id": 5, "mae_id": 6, "genero": "M"},
    {"id": 12, "nome": "Camila", "pai_id": 5, "mae_id": 6, "genero": "F"},
    {"id": 13, "nome": "Lucas", "pai_id": 7, "mae_id": 8, "genero": "M"},
    {"id": 14, "nome": "Marina", "pai_id": 7, "mae_id": 8, "genero": "F"},
    {"id": 15, "nome": "Felipe", "pai_id": 9, "mae_id": 10, "genero": "M"},
    {"id": 16, "nome": "Juliana", "pai_id": 9, "mae_id": 10, "genero": "F"},
    {"id": 17, "nome": "Vitor", "pai_id": 5, "mae_id": 6, "genero": "M"},
    {"id": 18, "nome": "Lívia", "pai_id": 7, "mae_id": 8, "genero": "F"},
    {"id": 19, "nome": "André", "pai_id": 7, "mae_id": 8, "genero": "M"},
    {"id": 20, "nome": "Beatriz", "pai_id": 5, "mae_id": 6, "genero": "F"},
    {"id": 21, "nome": "Henrique", "pai_id": 5, "mae_id": 6, "genero": "M"},
    {"id": 22, "nome": "Natália", "pai_id": 9, "mae_id": 10, "genero": "F"},
    {"id": 23, "nome": "Otávio", "pai_id": 9, "mae_id": 10, "genero": "M"},
    {"id": 24, "nome": "Sofia", "pai_id": 7, "mae_id": 8, "genero": "F"},
    {"id": 25, "nome": "Pedro", "pai_id": 9, "mae_id": 10, "genero": "M"},
]

# Criar dicionário de nós
id_to_node = {}
for pessoa in familia_estendida:
    label = f"{pessoa['nome']} ({pessoa['genero']})"
    id_to_node[pessoa["id"]] = Node(label)

# Definir pai como o nó pai principal
for pessoa in familia_estendida:
    if pessoa["pai_id"]:
        id_to_node[pessoa["id"]].parent = id_to_node[pessoa["pai_id"]]

# Encontrar uma raiz da árvore
raiz = next(node for node in id_to_node.values() if node.is_root)

# Função para colorir por geração
def cor_por_nivel(nivel):
    cores = ["#d0f0c0", "#add8e6", "#ffcccb", "#e6e6fa", "#f0e68c"]
    return cores[nivel % len(cores)]

# Função para atributos personalizados do nó
def node_attrs_func(node):
    nivel = node.depth
    color = cor_por_nivel(nivel)
    return f'label="{node.name}\\nGeração {nivel}", style=filled, fillcolor="{color}"'

# Exportar e renderizar com Graphviz
from graphviz import Source

dot_path = "arvore_hierarquica_com_geracoes.dot"
png_path = "arvore_hierarquica_com_geracoes.png"

DotExporter(raiz, nodeattrfunc=node_attrs_func).to_dotfile(dot_path)

# Renderiza com graphviz
s = Source.from_file(dot_path)
s.render(png_path, format="png", cleanup=True)

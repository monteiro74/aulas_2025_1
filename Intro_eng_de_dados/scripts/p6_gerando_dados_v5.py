# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p6_gerando_dados.py
# Descrição: Este script gera dados fictícios (nome, idade e renda) e
#            depois e grava em formato csv, para uso posterior.
#
# Autor: Nome do aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados e leitura do arquivo CSV.
#
# Uso: Rode este programa usando uma IDE Python
# ==============================================================================

import pandas as pd

# Dados fictícios de 30 registros
dados = {
    'Nome': [
        'João Silva', 'Maria Oliveira', 'Carlos Pereira', 'Ana Santos', 'Lucas Costa',
        'Fernanda Almeida', 'Paula Rocha', 'Rodrigo Martins', 'Gabriel Souza', 'Larissa Lima',
        'Beatriz Silva', 'Vinícius Oliveira', 'Camila Ferreira', 'André Santos', 'Juliana Costa',
        'Ricardo Almeida', 'Mariana Rocha', 'Eduardo Martins', 'Patrícia Souza', 'Rafael Lima',
        'Júlia Silva', 'Gustavo Oliveira', 'Tatiane Pereira', 'Diego Santos', 'Fernanda Rocha',
        'Roberta Almeida', 'Marta Silva', 'Vinícius Costa', 'Tiago Pereira', 'Cássia Lima'
    ],
    'Idade': [
        22, 34, 28, 40, 25, 32, 29, 45, 23, 41,
        30, 38, 27, 36, 33, 24, 37, 29, 42, 31,
        35, 39, 26, 33, 28, 41, 32, 30, 37, 44
    ],
    'Renda': [
        3000, 5000, 4000, 6000, 3500, 5500, 4200, 7000, 3800, 6200,
        4800, 5200, 4500, 5900, 5000, 3700, 5600, 4300, 6500, 5100,
        5400, 6000, 4600, 4900, 5300, 5700, 5100, 4800, 5300, 6500
    ]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Exibindo as primeiras linhas do dataset
print(df)

# Para salvar o dataset como um arquivo CSV com ";" como delimitador
df.to_csv("clientes.csv", index=False, sep=";")

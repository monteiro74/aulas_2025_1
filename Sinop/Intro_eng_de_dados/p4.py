# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p3.py - Aplicação do algoritmo Apriori
# Descrição: Este script carrega um arquivo CSV, verifica via o algoritmo
#            apriori se existem padrões na compra de produtos.
#
# Autor: Nome do aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados e leitura do arquivo CSV.
# - apriori: É o algoritmo que busca encontrar padrões frequentes 
# - association_rules: regras de associação entre os itens
# - TransactionEncoder  converte a lista de itens em uma matriz binária 
#
# Uso: Coloque o dataset na mesma pasta que este programa
# pip install mlxtend
# Cabeçalho explicativo sobre as colunas:
# 'antecedents': Itens no lado esquerdo da regra (condição ou item inicial)
# 'consequents': Itens no lado direito da regra (resultado ou item esperado)
# 'support': A probabilidade de que os itens na regra apareçam juntos no dataset (suporte)
# 'confidence': A probabilidade de que o consequente ocorra dado o antecedente (confiança)
# 'lift': A medida de correlação entre antecedente e consequente. Indica a relação entre os itens comparando com sua ocorrência esperada.
#
# ==============================================================================
import pandas as pd  # Importação do pandas
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


# 1. Carregar o dataset2.csv
df = pd.read_csv('dataset2.csv')

# 2. Converter a coluna 'Itens' em uma lista de transações
dataset = df['Itens'].str.split(',').tolist()

# 3. Transformar o dataset para um formato adequado para o algoritmo Apriori
te = TransactionEncoder()
te_ary = te.fit_transform(dataset)  # Transformando os dados para o formato binário
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)  # Criando um DataFrame com os dados binários

# 4. Aplicar o Algoritmo Apriori com um min_support ajustado
frequent_itemsets = apriori(df_encoded, min_support=0.1, use_colnames=True)

# Verificar se foram encontrados itemsets frequentes
if frequent_itemsets.empty:
    print("Nenhum itemset frequente encontrado.")
else:
    # 5. Gerar regras de associação
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    # 6. Adicionar coluna de Interpretacao com base no 'lift'
    def interpretar_lift(lift_value):
        if lift_value < 1:
            return "Relacao negativa"
        elif lift_value == 1:
            return "Sem relacao"
        else:
            return "Relacao positiva"

    # Aplicar a função de Interpretacao
    rules['Interpretacao'] = rules['lift'].apply(interpretar_lift)

    # 7. Exibir os itemsets frequentes de forma legível
    print("Itemsets Frequentes:")
    print(frequent_itemsets.sort_values(by="support", ascending=False).reset_index(drop=True))
    print("\n" + "-"*50 + "\n")

    # 8. Exibir as regras de associação de forma legível
    if rules.empty:
        print("Nenhuma regra de associação encontrada.")
    else:
        print("Regras de Associação:")
        # Ajustar o nome da coluna para corresponder à criação de 'Interpretacao'
        print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift', 'Interpretacao']].sort_values(by="lift", ascending=False).reset_index(drop=True))
    
        # 9. Melhorar a saída CSV com delimitador adequado para Excel
        # Ajustar as listas 'antecedents' e 'consequents' para serem armazenadas como string
        rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
        rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))
        
        # Salvar o resultado em um arquivo CSV
        rules[['antecedents', 'consequents', 'support', 'confidence', 'lift', 'Interpretacao']].to_csv('probabilidade_de_ocorrencia.csv', index=False, sep=';', encoding='utf-8')
    
        print("\nResultado salvo em 'probabilidade_de_ocorrencia.csv'")

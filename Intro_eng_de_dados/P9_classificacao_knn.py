# -*- coding: utf-8 -*-
# ==============================================================================
# Nome do Script: p8_DBScan.py
#
# Descrição: Este script gera uma tabela com um campo novo chamado classe prevista
#            e a saída é gravada em um arquivo csv, ele implementa a classificação
#            usando k-nn.
#
# Autor: Nome do aluno
# Data de Criação: 
# Hora de Criação: 
#
# Dependências:
# - pandas: Para manipulação de dados e leitura do arquivo CSV.
# - sklearn: Biblioteca para aprendizado de máquina.
#
# Uso: Rode este programa na mesma pasta com o arquivo clientes.csv
# ==============================================================================

# 1. Importando bibliotecas necessárias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 2. Carregar o dataset
# Assumindo que 'clientes.csv' está no mesmo diretório do script
# O arquivo usa ';' como delimitador
df = pd.read_csv('clientes.csv', delimiter=';')

# 3. Visualizar as primeiras linhas do dataset
print("Primeiras linhas do dataset:")
print(df.head())

# 4. Criar uma coluna 'classe' com base na 'Renda', por exemplo:
# Se a renda for maior que 5000, classifica como "Alta Renda", caso contrário "Baixa Renda"
df['classe'] = df['Renda'].apply(lambda x: 'Alta Renda' if x > 5000 else 'Baixa Renda')

# 5. Agora temos 'Nome', 'Idade', 'Renda' e 'classe'
# Podemos usar 'Idade' e 'Renda' como variáveis independentes (X)
# E 'classe' como a variável dependente (y)

# 6. Separando variáveis independentes (X) e a variável dependente (y)
X = df[['Idade', 'Renda']]  # Exemplo de características
y = df['classe']  # Classe a ser prevista

# 7. Dividir os dados em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Padronizar os dados (importante para o K-NN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 9. Inicializar o classificador K-NN
# Vamos usar 3 vizinhos, você pode ajustar esse valor para melhorar os resultados
knn = KNeighborsClassifier(n_neighbors=3)

# 10. Treinar o modelo com os dados de treino
knn.fit(X_train, y_train)

# 11. Fazer previsões com os dados de teste
y_pred = knn.predict(X_test)

# 12. Avaliar a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)

print(f"Acurácia do modelo K-NN: {accuracy * 100:.2f}%")

# 13. Exibir a classificação de todos os clientes no dataset
# Aplicando o modelo a todo o dataset (não apenas ao conjunto de teste)
clientes_classificados = df[['Nome', 'Idade', 'Renda']].copy()  # Criar uma cópia das colunas que queremos exibir
clientes_classificados['Classe Prevista'] = knn.predict(scaler.transform(df[['Idade', 'Renda']]))  # Previsão da classe

# 14. Exibir o resultado na tela
print("\nClassificação de todos os clientes:")
print(clientes_classificados)

# 15. Gravar o dataframe com as classificações em um novo arquivo CSV
clientes_classificados.to_csv('clientes_classificados.csv', index=False, sep=';')

print("\nClassificação dos clientes foi salva em 'clientes_classificados.csv'.")

# 16. Exemplo de previsão para novos dados (caso queira testar com novos dados)
# Suponha que queremos prever a classe para um cliente com 30 anos e renda de 4000
#novo_cliente = [[30, 4000]]
#novo_cliente = scaler.transform(novo_cliente)  # Não se esqueça de escalar!

# 17. Predizendo a classe do novo cliente
#classe_predita = knn.predict(novo_cliente)
#print(f"A classe do novo cliente é: {classe_predita[0]}")


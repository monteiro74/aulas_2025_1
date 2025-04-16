# Lista de exercícios:


---
## Exercíco E1:

* Crie um banco de dados com MySQL (ou MariaDB)
* Importe os dados de: https://github.com/monteiro74/aulas_2025_1/tree/main/Intro_eng_de_dados/dados_receita_federal
* Em caso de dúvida use o dicionários de dados para criar as tabelas se for o caso e renomear campos: https://www.gov.br/receitafederal/dados/cnpj-metadados.pdf

E1.1. Após importar os dados, use as ferramentas DBeaver, myphpadmin ou MySQL Workbench, para gerar o diagrama entidade relacionamento dos dados abertos da Receita Federal.
Use como referência o diagrama: https://raw.githubusercontent.com/aphonsoar/Receita_Federal_do_Brasil_-_Dados_Publicos_CNPJ/refs/heads/master/Dados_RFB_ERD.png

E1.2. Qual o tamanho total do banco de dados após importação?

E1.3. Como importar as demais tabelas do conjunto de dados abertos da Receita Federal (https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/2025-03/) para atualizar a tabela empresas ?

E1.4. Para a tabela estabelecimentos_export.csv, corrija os nomes dos campos usando o dicionário de dados

---
## Exercício E2:

Utilize os **dataset1.csv** e **dataset2.csv** e a IDE Spyder (**contindo no Anaconda**)

E2.1. Salve os dataset1.csv e dataset2.csv em uma pasta no seu disco.

E2.2. Execute o script p1.py

E2.3. Execute o script p2.py

E2.4. Execute o script p3.py

E2.5. Execute o script p4.py

E2.6. Execute o script p5.py

E2.7. Execute o script p6_gerando_dados_v5.py.py

E2.8. Execute o script p7_k-means_v5.py

E2.9. Execute o script metodo_cotovelo_v5.py

E2.10. Execute o script metodo_silueta_v5.py

E2.11. Execute o script p8_DBScan_v5.py.py

E2.12. Execute o script p9_classificacao_knn.py.py

E2.13. Altere os scripts acima para que todos possam:

E2.13.1. Informar a hora com minutos e segundos de início de processamento, na tela.

E2.13.2. Informar a hora com minutos e segundos de fim de processamento, na tela.

E2.13.3. Informar a hora com minutos e segundos com o tempo total de processamento, na tela.

---
## Exercício E3:

Use o mesmo banco de dados utilizado em E1.

* Faça download do Pentaho PDI (https://pentaho.com/pentaho-developer-edition/)
* Configure as variáveis de ambiente para rodar o Pentaho (https://agail.com.br/2020/12/05/tutorial-para-instalar-o-pentaho-data-integration-ce-no-windows/)

E3.1. Importe os dados do arquivo clientes.csv (https://raw.githubusercontent.com/monteiro74/aulas_2025_1/refs/heads/main/Intro_eng_de_dados/clientes.csv)

E3.2. Execute a exportação de dados (do arquivo csv para o mysql) (dica: use o arquivo Transformação_exportar_pdi.ktr)

E3.3. Execute a importação de dados (do mysql para o csv) (dica: use o arquivo Transformação_importar_pdi.ktr)

Observação:
* Se necessário faça download do drivers JDBC para MySQL: https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-j-9.3.0.tar.gz
* Se necessário faça download do driver ODBC para MySQL: https://dev.mysql.com/get/Downloads/Connector-ODBC/9.3/mysql-connector-odbc-9.3.0-winx64.msi

---
## Exercício E4: 

Utilize o Orange Data Mining (**contindo no Anaconda**)

E4.1. baixe o arquivo clientes.csv (https://raw.githubusercontent.com/monteiro74/aulas_2025_1/refs/heads/main/Intro_eng_de_dados/clientes.csv)

E4.2. Execute o pipeline knn_tree_barplot.ows 		(https://github.com/monteiro74/aulas_2025_1/blob/main/Intro_eng_de_dados/knn_tree_barplot.ows)

E4.3. Execute o pipeline agrupamento_clusterizacao.ows 	(https://github.com/monteiro74/aulas_2025_1/blob/main/Intro_eng_de_dados/agrupamento_clusterizacao.ows)

---
## Exercício E5:

E5.1. Crie um banco de dados preparado para receber dados do transacional

E5.2. Execute o script script_sql_snowflake.sql

E5.3. Faça o diagrama ER do novo banco (use o MySQL Wordkbench, DBeaver ou phpMyAdmin)

---
## Exercício E6:

Crie um prompt com o chatgpt para fazer o seguinte: 
* Escrever um programa em python
* ler os dados do dataset clientes.csv
* Apresente na tela um gráfico com idade x renda
* Use o streamlit.

---
## Exercício E7: 

Após a importação dos dados abertos da Receite Federal (no exercício E1):

* Crie representações gráficas no Power BI com as tabelas importadas
* Use o driver ODBC para conectar o PowerBI no MySQL. 
* Exemplo: https://raw.githubusercontent.com/monteiro74/aulas_2025_1/refs/heads/main/Intro_eng_de_dados/exercicio_powerbi1.png


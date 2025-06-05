import pyodbc
import pandas as pd
from sklearn.model_selection import train_test_split  # Função para dividir os dados em treino e teste
from sklearn.linear_model import LinearRegression    # Classe para criar e treinar um modelo de Regressão Linear
from sklearn.metrics import mean_squared_error       # Função para calcular o erro quadrático médio (MSE) do modelo
from sklearn.preprocessing import LabelEncoder       # Classe para codificar dados categóricos em valores numéricos


# Função para conectar e ler dados do banco
def conectar_e_ler_dados():
    server = ''  # Nome ou IP do servidor SQL Server
    database = ''  # Nome do banco de dados
    username = ''  # Usuário do banco
    password = ''  # Senha do banco

    try:
        # Conectando ao SQL Server
        connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        )
        print("Conexão bem-sucedida!")

        # Lendo os dados da tabela para um DataFrame
        query = "SELECT IdPet, Apelido, Raca, IdAluno, Valor FROM [dbo].[tblPets]"
        df = pd.read_sql(query, connection)

        # Fechando a conexão
        connection.close()

        return df

    except pyodbc.Error as e:
        print("Erro ao conectar ao SQL Server:", e)
        return None

# Função para aprendizado de máquina
def aprendizado_maquina(df):
    # Preenchendo valores nulos
    df['IdAluno'] = df['IdAluno'].fillna(-1)  # Substitui valores nulos de IdAluno por -1

    # Codificando a coluna categórica 'Raca'
    le_raca = LabelEncoder()
    df['Raca'] = le_raca.fit_transform(df['Raca'])

    # Separando variáveis independentes (X) e dependente (y)
    X = df[['Raca', 'IdAluno']]
    y = df['Valor']

    # Dividindo os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Criando e treinando o modelo
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Fazendo previsões no conjunto de teste
    y_pred = model.predict(X_test)

    # Avaliando o modelo
    mse = mean_squared_error(y_test, y_pred)
    print(f"Erro quadrático médio (MSE): {mse:.2f}")
    print("Coeficientes do modelo:", model.coef_)
    print("Intercepto do modelo:", model.intercept_)

# Fluxo principal
if __name__ == "__main__":
    # Conectando e lendo dados do SQL Server
    df = conectar_e_ler_dados()

    if df is not None:
        print("Dados da tabela:")
        print(df)

        # Executando aprendizado de máquina
        aprendizado_maquina(df)
# --- Cria o banco de dados ------------------
CREATE DATABASE marmita;

# --- Seleciona o banco de dados para uso ------------------
USE marmita;

# --- Mostra a relação de processos internos no momento ------------------
SHOW PROCESSLIST;

# --- Apresenta o conjunto de permissões do usuário atual ------------------
SHOW GRANTS;

# --- Mostra informações sobre collation e charset disponíveis ------------------
SHOW COLLATION;

# --- Filtra as collations para o conjunto de caracteres utf8mb4 ------------------
SHOW COLLATION WHERE Charset = 'utf8mb4';

# --- Mostra apenas a collation padrão do banco ------------------
SHOW COLLATION WHERE `Default` = 'Yes';

# --- Mostra o conjunto de caracteres padrão do banco de dados ------------------
SELECT default_character_set_name 
FROM information_schema.SCHEMATA  
WHERE schema_name = "marmita";

# --- Exibe a configuração atual do conjunto de caracteres do banco de dados ------------------
SHOW VARIABLES LIKE "character_set_database";

# --- No momento, não há tabelas para exibir o status ------------------
SHOW TABLE STATUS;

# --- No momento, não há tabelas para listar ------------------
SHOW TABLES;

# --- Criação da tabela pet ------------------
CREATE TABLE pet (
    apelido VARCHAR(20) NOT NULL,  # Nome do animal
    dono VARCHAR(20) NOT NULL,  # Nome do dono
    especie VARCHAR(20) NOT NULL,  # Espécie do animal (Cão, Gato, etc.)
    sexo CHAR(1) NOT NULL,  # Sexo (M ou F)
    nascimento DATE NOT NULL,  # Data de nascimento do animal
    morte DATE DEFAULT NULL,  # Data de falecimento (pode ser nulo)
    PRIMARY KEY (apelido, dono)  # Definição de chave primária composta
);

# --- Lista as tabelas existentes após a criação ------------------
SHOW TABLES;

# --- Criação da tabela pessoas ------------------
CREATE TABLE pessoas (
    IDPessoa INT AUTO_INCREMENT PRIMARY KEY,  # Identificador único
    Nome VARCHAR(100) NOT NULL,  # Nome da pessoa
    Nascimento DATE NOT NULL,  # Data de nascimento
    Bairro VARCHAR(50) NOT NULL,  # Bairro onde reside
    UF CHAR(2) NOT NULL,  # Unidade federativa
    Cidade VARCHAR(255) NOT NULL  # Cidade onde reside
);

# --- Mostra detalhes das tabelas criadas ------------------
DESCRIBE pessoas;
DESCRIBE pet;

# --- Exibe as tabelas existentes ------------------
SHOW TABLES;

# --- Exibe as colunas da tabela pessoas ------------------
SHOW COLUMNS FROM pessoas;

# --- Insere dados na tabela pet ------------------
INSERT INTO pet (apelido, dono, especie, sexo, nascimento) 
VALUES 
('REX', 'ANA', 'CÃO', 'M', '2010-10-26'),
('SNOOPY', 'BOB', 'CÃO', 'M', '2014-11-22'),
('GARFIELD', 'CLARA', 'GATO', 'M', '2013-12-27');

# --- Insere dados na tabela pessoas ------------------
INSERT INTO pessoas (IDPessoa, Nome, Nascimento, Bairro, UF, Cidade)
VALUES 
(1, 'ANA', '1985-10-23', 'Centro', 'SP', 'Rancharia'),
(2, 'BOB', '1990-11-25', 'Porto', 'MT', 'Cuiabá'),
(3, 'CLARA', '1992-12-21', 'Porto', 'MT', 'Vacaria');

# --- Consultas básicas na tabela pet ------------------
SELECT * FROM pet;
SELECT apelido, dono FROM pet;
SELECT apelido, sexo, nascimento FROM pet WHERE dono = 'ANA';
SELECT apelido, nascimento FROM pet WHERE nascimento > '2010-10-26';
SELECT * FROM pet WHERE dono = 'BOB' AND sexo = 'M';

# --- Atualiza um registro na tabela pet ------------------
UPDATE pet 
SET especie = 'LAGARTO', morte = '2016-01-27' 
WHERE apelido = 'REX';

# --- Confirmação da atualização ------------------
SELECT * FROM pet;

# --- Remove um registro específico da tabela pet ------------------
DELETE FROM pet WHERE apelido = 'REX';

# --- Verifica os registros restantes ------------------
SELECT * FROM pet;

# --- Remove todos os registros da tabela pet ------------------
DELETE FROM pet;

# --- Confirma que a tabela está vazia ------------------
SELECT * FROM pet;

# --- Exclui a tabela pet ------------------
DROP TABLE pet;

# --- Exibe as tabelas existentes após a exclusão ------------------
SHOW TABLES;

# --- Criação da tabela dependentes com chave estrangeira ------------------
CREATE TABLE dependentes (
    IDDependente INT AUTO_INCREMENT PRIMARY KEY,  # Identificador único
    NomeD VARCHAR(100) NOT NULL,  # Nome do dependente
    IDPessoa INT NOT NULL,  # Chave estrangeira para a tabela pessoas
    FOREIGN KEY (IDPessoa) REFERENCES pessoas(IDPessoa) ON DELETE CASCADE
);

# --- Exibe as tabelas existentes ------------------
SHOW TABLES;

# --- Adiciona índices à tabela pessoas ------------------
ALTER TABLE pessoas ADD INDEX IDPessoa_idx (IDPessoa);
ALTER TABLE pessoas ADD INDEX UF_idx (UF);

# --- Insere mais dados na tabela pessoas ------------------
INSERT INTO pessoas (IDPessoa, Nome, Nascimento, Bairro, UF, Cidade) 
VALUES 
(4, 'Pessoa 1', '1990-01-01', 'Bairro 1', 'SP', 'Cidade A'),
(5, 'Pessoa 2', '1985-05-05', 'Bairro 2', 'RJ', 'Cidade B');

# --- Insere dados na tabela dependentes ------------------
INSERT INTO dependentes (IDDependente, NomeD, IDPessoa) 
VALUES 
(1, 'Filho1', 2),
(2, 'Filho2', 2),
(3, 'Filho3', 5);

# --- Consultas para verificar os dados inseridos ------------------
SELECT * FROM dependentes;
SELECT * FROM pessoas;

# --- Exibe a estrutura das tabelas ------------------
DESCRIBE pessoas;
DESCRIBE dependentes;

# --- Mostra as colunas das tabelas ------------------
SHOW COLUMNS FROM pessoas;
SHOW COLUMNS FROM dependentes;

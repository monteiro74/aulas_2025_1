CREATE DATABASE aula3;

SHOW DATABASE;

USE aula3;

SHOW PROCESSLIST;

SHOW GRANTS;

SHOW COLLATION;

SHOW COLLATION WHERE Charset = 'utf8mb4';

SHOW COLLATION WHERE `Default` = 'Yes';

SELECT default_character_set_name FROM information_schema.SCHEMATA  WHERE schema_name = "aula3";

SHOW VARIABLES LIKE "character_set_database";

SELECT SCHEMA_NAME 'aula3', default_character_set_name 'charset', DEFAULT_COLLATION_NAME 'collation' FROM information_schema.SCHEMATA;

SHOW TABLE STATUS;

SHOW TABLES;

CREATE TABLE pet (
apelido VARCHAR(20),
dono VARCHAR(20),
especie VARCHAR(20),
sexo CHAR(1),
nascimento DATE,
morte DATE
);

SHOW TABLES;

CREATE TABLE pessoas (
IDPessoa int,
Nome varchar(100),
Nascimento date,
Bairro varchar(50),
UF varchar(2),
Cidade varchar(255)
);

DESCRIBE pessoas;

DESCRIBE pet;

SHOW TABLES;

SHOW COLUMNS FROM pessoas;

INSERT INTO pet (apelido, dono, especie, sexo, nascimento) VALUES ('REX','ANA','CAO','M','2010-10-26');
INSERT INTO pet (apelido, dono, especie, sexo, nascimento) VALUES ('SNOOPY','BOB','CAO','M','2014-11-22');
INSERT INTO pet (apelido, dono, especie, sexo, nascimento) VALUES ('GARFIELD','CLARA','GATO','M','2013-12-27');

INSERT INTO pessoas (IDPessoa, Nome, Nascimento, Bairro, UF, Cidade)VALUES ('1','ANA','2015-10-23','Centro','SP','Rancharia');
INSERT INTO pessoas (IDPessoa, Nome, Nascimento, Bairro, UF, Cidade) VALUES ('2','BOB','2015-11-25','Porto','MT','Cuiaba');
INSERT INTO pessoas (IDPessoa, Nome, Nascimento, Bairro, UF, Cidade) VALUES ('3','Clara','2014-12-21','Porto','MT','Vacaria');

SELECT * FROM pet;

SELECT apelido, dono FROM pet;

SELECT apelido, sexo, nascimento FROM pet WHERE dono='ANA';

SELECT apelido, nascimento FROM pet WHERE nascimento > '2010-10-26';

SELECT * FROM pet WHERE dono='BOB' and sexo='M';

UPDATE pet SET especie='LAGARTO', morte='2016-01-27' WHERE apelido='REX';

SELECT * FROM pet;

DELETE FROM pet WHERE apelido='REX';

SELECT * FROM pet;

DELETE FROM  pet;

SELECT * FROM pet;

DROP TABLE pet;

SHOW TABLES;

CREATE TABLE dependentes(
IDDependente int,
NomeD varchar(100)
);

SHOW TABLES;

ALTER TABLE dependentes ADD IDPessoa Int;

SHOW COLUMNS FROM dependentes;

DESCRIBE dependentes;

-- ALTER TABLE pessoas ADD PRIMARY KEY (IDPessoa);
ALTER TABLE dependentes ADD FOREIGN KEY (IDPessoa) REFERENCES pessoas(IDPessoa);

SHOW COLUMNS FROM dependentes;

DESCRIBE dependentes;

ALTER TABLE pessoas ADD INDEX IDPessoa_idx (IDPessoa);

ALTER TABLE pessoas ADD INDEX UF_idx (UF);

DESCRIBE pessoas;

INSERT INTO dependentes (IDDependente, NomeD, IDPessoa) VALUES ('1','Filho1','2');
INSERT INTO dependentes (IDDependente, NomeD, IDPessoa) VALUES ('2','Filho2','2');

SELECT * FROM dependentes

INSERT INTO dependentes (IDDependente, NomeD, IDPessoa) VALUES ('3','Filho3','5');

SELECT * FROM dependentes
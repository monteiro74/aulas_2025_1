-- Crie um banco de dados
CREATE DATABASE cafe

-- O comando USE é usado quando existem multiplos bancos de dados e
-- queremos especificar o banco de trabalho atual
USE cafe

-- O comando GO informa o SQL Server que deve interpretar as instru��es a seguir
GO

-- Criar a tabela alunos
CREATE TABLE tblAlunos 
(
 IdAluno int IDENTITY(1,1) PRIMARY KEY NOT NULL,
 Nome varchar(100) NOT NULL,
 Aniversario date NOT NULL,
 Sexo varchar(1) NOT NULL, -- M ou F
 Salario decimal(10,2) NOT NULL,
);

-- Alterar a tabela para suportar um campo auto increment
-- ALTER TABLE tblAlunos DROP COLUMN IdAluno
-- ALTER TABLE tblAlunos ADD IdAluno INT IDENTITY(1,1)
-- o comando DROP deleta a tabela
-- DROP TABLE tblAlunos
-- IDENTITY(1,1) (a cl�usula identity � usada para criar um campo autoincrement
-- Identity increment = 1
-- Identity seed = 1

-- Inserir dados na tabela Alunos
INSERT INTO tblAlunos VALUES ('ANA', '19971231', 'F', 5000);
INSERT INTO tblAlunos VALUES ('BOB', '19980522', 'M', 2500.50);
INSERT INTO tblAlunos VALUES ('BILL', '19950715', 'M', 3500.50);
INSERT INTO tblAlunos VALUES ('CLARA', '19810817', 'F', 4000.50);
INSERT INTO tblAlunos VALUES ('DANIEL', '20031125', 'M', 3500);
INSERT INTO dbo.tblAlunos VALUES ('DANIELA', '20031220', 'F', 5500);

-- Selecionar os primeiros 1000 registros da tabela Alunos
SELECT TOP (1000) [IdAluno]
      ,[Nome]
      ,[Aniversario]
      ,[Sexo]
      ,[Salario]
  FROM [escola2].[dbo].[tblAlunos]

-- Selecionar todos os registros da tabela Alunos
SELECT * FROM tblAlunos

-- Qual o resultado do comando abaixo?
INSERT INTO tblAlunos VALUES (2, 'DANIEL', '20031125', 'F', 3670);
-- Qual o motivo do erro??

-- Cria a tabela usada para informar se o aluno esteve presente ou faltou
CREATE TABLE tblSituacao
(
 IdSituacao int PRIMARY KEY NOT NULL,
 Situacao varchar(30) NOT NULL
);

-- Deletar a tabela situacao
-- DROP TABLE tblSituacao

-- Inserir dados na tabela situacao
INSERT INTO tblSituacao VALUES (1, 'MATRICULADO');
INSERT INTO tblSituacao VALUES (2, 'CURSANDO');
INSERT INTO tblSituacao VALUES (3, 'APROVADO');
INSERT INTO tblSituacao VALUES (4, 'REPROVADO');
INSERT INTO tblSituacao VALUES (5, 'SUSPENSO');
INSERT INTO tblSituacao VALUES (6, 'CANCELADO');

-- Selecionar todos os registros da tabela Situacao
SELECT * FROM tblSituacao

-- Criar a tabela cursos
CREATE TABLE tblCursos
(
 IdCurso int PRIMARY KEY NOT NULL,
 NomeCurso varchar(50) NOT NULL
);

-- Inserir dados na tabela Cursos
INSERT INTO tblCursos VALUES (1, 'PROGRAMACAO C++');
INSERT INTO tblCursos VALUES (2, 'BANCO DE DADOS 1');
INSERT INTO tblCursos VALUES (3, 'SISTEMAS OPERACIONAIS');
INSERT INTO tblCursos VALUES (4, 'REDES 2');

-- Deletar a tabela cursos
-- DROP TABLE tblCursos

-- Selecionar todos os registros da tabela Cursos
SELECT * FROM tblCursos

-- Criar a tabela turmas
CREATE TABLE tblTurmas
(
 IdTurma int IDENTITY(1,1) PRIMARY KEY NOT NULL,
 IdAluno int NOT NULL,
 IdCurso int NOT NULL,
 DescricaoTurma varchar(50) NOT NULL,
 PrecoTurma numeric(15,2) NOT NULL,
 DataInicio date NOT NULL,
 DataFim date
);

-- Deletar a tabela turmas
-- DROP TABLE tblTurmas

-- Inserir dados na tabela Turmas
INSERT INTO tblTurmas VALUES (1, 1, 'C++ DE F�RIAS', 1250.50, '20231025', '20231029');
INSERT INTO tblTurmas VALUES (1, 2, 'C++ DE F�RIAS', 1250.50, '20231025', '20231029');
INSERT INTO tblTurmas VALUES (1, 3, 'C++ DE F�RIAS', 0, '20231025', '20231029');

-- Selecionar todos os registros da tabela Turmas
SELECT * FROM tblTurmas

-- Criar a tabela Presen�as
CREATE TABLE tblPresencas
(
 IdTurma int NOt NULL,
 IdAluno int NOT NULL,
 IdSituacao int NOT NULL,
 DataPresenca date NOT NULL
);

-- Inserir alguns registros como exemplo
INSERT INTO tblPresencas VALUES (1, 1, 2, '20231026');
INSERT INTO tblPresencas VALUES (1, 2, 2, '20231026');
INSERT INTO tblPresencas VALUES (1, 3, 2, '20231026');

-- Deletar a tabela presencas
-- DROP TABLE tblPresencas

/* Para deletar todas as tabelas:
DROP TABLE tblAlunos;
DROP TABLE tblSituacao;
DROP TABLE tblCursos;
DROP TABLE tblTurmas;
DROP TABLE tblPresencas;
*/

-- Os comandos ALTER TABLE abaixo criam os relacionamentos entre as tabelas
-- na tabela de turmas adicionar uma FK para a tabela alunos
ALTER TABLE tblTurmas
  ADD CONSTRAINT fk_TurmasAlunos FOREIGN KEY (IdAluno) REFERENCES tblAlunos(IdAluno);

-- Na tabela de turmas adicionar uma FK para a tabela cursos
ALTER TABLE tblTurmas
  ADD CONSTRAINT fk_TurmasCursos FOREIGN KEY (IdCurso) REFERENCES tblCursos(IdCurso);

-- Na tabela de presenca adicionar uma FK para a tabela turmas
ALTER TABLE tblPresencas
  ADD CONSTRAINT fk_PresencaTurma FOREIGN KEY (IdTurma) REFERENCES tblTurmas(IdTurma);

-- Na tabela de presenca adicionar uma FK para a tabela aluno
ALTER TABLE tblPresencas
  ADD CONSTRAINT fk_PresencaAluno FOREIGN KEY (IdAluno) REFERENCES tblAlunos(IdAluno);

-- Na tabela de presenca adicionar uma FK para a tabela situacao
ALTER TABLE tblPresencas
  ADD CONSTRAINT fk_PresencaSituacao FOREIGN KEY (IdSituacao) REFERENCES tblSituacao(IdSituacao);

-- Count realiza a contagem de registros
SELECT COUNT(IdTurma) as qtdeTurma FROM tblTurmas;

-- Realizar a soma de valores (em um campo num�rico)
SELECT SUM(PrecoTurma) AS somaPreco FROM tblTurmas;

-- Mostrar a m�dia de valores da coluna
SELECT AVG(Salario) AS mediaSalario FROM tblAlunos;

-- Mostrar o maior valor da coluna
SELECT MAX(Salario) AS maxSalario FROM tblAlunos;

-- Mostrar o menor valor da coluna
SELECT MIN(Salario) AS minSalario FROM tblAlunos;

-- Select com e sem distinc, distinct apresent um registro n�o repetido
SELECT DescricaoTurma FROM tblTurmas;
SELECT DISTINCT(DescricaoTurma) FROM tblTurmas;

-- Criando a tabela Pets
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tblPets](
	[IdPet] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
	[Apelido] [nvarchar](50) NULL,
	[Raca] [nvarchar](30) NULL,
	[IdAluno] [int] NULL,
	[Valor] [decimal](18, 0) NULL
) ON [PRIMARY];

-- Inserir dados na tabela pet
INSERT INTO tblPets ([Apelido],[Raca],[IdAluno],[Valor]) VALUES('DOG1', 'CACHORRO', 1 ,1500.00);

-- Deletar todos os registros da tabela pets
DELETE FROM tblPets;

-- Confirmar que houve dele��o de todos os registros da tabela pets
SELECT * FROM tblPets;

-- Apagar a tabela pets
DROP TABLE tblPets;

-- Recriando a tabela pets
CREATE TABLE [dbo].[tblPets](
	[IdPet] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
	[Apelido] [nvarchar](50) NULL,
	[Raca] [nvarchar](30) NULL,
	[IdAluno] [int] NULL,
	[Valor] [decimal](18, 0) NULL
) ON [PRIMARY];

-- Inserir registros na tabela pets
INSERT INTO tblPets ([Apelido],[Raca],[IdAluno],[Valor]) VALUES('DOG1', 'MASTIN', 1 ,1500.00);
INSERT INTO tblPets ([Apelido],[Raca],[IdAluno],[Valor]) VALUES('DOG2', 'FILA', 2 ,2500.00);
INSERT INTO tblPets ([Apelido],[Raca],[IdAluno],[Valor]) VALUES('DOG3', 'BULDOGUE', 3 ,3500.00);
INSERT INTO tblPets ([Apelido],[Raca],[IdAluno],[Valor]) VALUES('CAT1', 'PERSA', 2 ,1800.00);
INSERT INTO tblPets ([Apelido],[Raca],[IdAluno],[Valor]) VALUES('CAT2', 'ANGORA', 2 ,2300.00);
INSERT INTO tblPets ([Apelido],[Raca],[IdAluno],[Valor]) VALUES('CAT3', 'SIAMES', 3 ,990.00);
INSERT INTO tblPets ([Apelido],[Raca],[Valor]) VALUES('CAT4', 'SIAMES',1000.00);
INSERT INTO tblPets ([Apelido],[Raca],[Valor]) VALUES('DOG4', 'FILA',2000.00);

-- Select com C�lculo, o campo valor tem 10% de desconto na compra a vista
SELECT  Apelido, Raca, IdAluno AS Dono, Valor, (Valor*0.90) AS valorVend_a_Vista FROM tblPets;

-- Select juntando 2 tabelas 
SELECT p.Apelido, p.Raca, p.Valor,
		a.Nome as Dono
FROM tblAlunos AS a, tblPets AS p
WHERE p.IdAluno = a.IdAluno;

-- Select com calculo
SELECT p.Apelido, p.Raca, p.Valor, 
       (p.Valor*0.90) AS valorVend_a_Vista,
	   a.Nome as Dono
FROM tblAlunos AS a, tblPets AS p
WHERE p.IdAluno = a.IdAluno;

-- Inner Joint
-- SELECT *
-- FROM tblAlunos a
-- INNER JOIN tblPets p
-- ON a.IdAluno = p.IdAluno
--
SELECT *
FROM tblAlunos a
INNER JOIN tblPets b
ON a.IdAluno = b.IdAluno;

-- Left outer join
SELECT *
FROM tblAlunos a
LEFT JOIN tblPets b
ON a.IdAluno = b.IdAluno;

-- Left outer join WHERE B.KEY IS NULL
SELECT *
FROM tblAlunos a
LEFT JOIN tblPets b
ON a.IdAluno = b.IdAluno
WHERE b.IdAluno IS NULL;

-- Full outer join
SELECT *
FROM tblAlunos a
FULL OUTER JOIN tblPets b
ON a.IdAluno = b.IdAluno;

-- Full outer join WHERE A.KEY IS NULL OR B.KEY IS NULL
SELECT *
FROM tblAlunos a
FULL OUTER JOIN tblPets b
ON a.IdAluno = b.IdAluno
WHERE a.IdAluno IS NULL OR b.IdAluno IS NULL;

-- Right outer join
SELECT *
FROM tblAlunos a
RIGHT JOIN tblPets b
ON a.IdAluno = b.IdAluno;

-- Right outer join WHERE A.KEY IS NULL
SELECT *
FROM tblAlunos a
RIGHT JOIN tblPets b
ON a.IdAluno = b.IdAluno
WHERE a.IdAluno IS NULL;

-- Select com group by, count e avg
SELECT Raca, 
	   AVG(Valor) AS mediaPreco,
	   COUNT(Raca) AS qtdeRaca
FROM tblPets
GROUP BY Raca
ORDER BY Raca;

-- Contar e agrupar os registros
SELECT Raca, count(IdPet) as quantidade_de_pets
FROM tblPets
GROUP BY Raca;

-- Contar os registros na tabela pets
SELECT count(IdPet) as quantidade_de_pets
FROM tblPets;

-- Select com HAVING, ORDER BY e ASC
SELECT Raca, Valor
FROM tblPets
GROUP BY Raca, Valor
HAVING SUM(Valor) > 1800
ORDER BY Valor ASC;

-- Select como calculadora
SELECT 500/2 AS valor;
SELECT 500*2 AS valor;
SELECT 500+200 AS valor;
SELECT 300+200 AS valor;
SELECT (500+500)*2/2+3 AS valor;
SELECT SQUARE(5) AS valor;
SELECT POWER(2,2) AS valor;
SELECT SQRT(35) AS valor;
SELECT pi() AS valorPI;

-- Mostrar a data atual do servidor
SELECT getdate() AS data_hora_atual;

-- Select com Distinct
SELECT DISTINCT Raca
FROM tblPets AS p;

-- Select com Count e Distinct
SELECT Count(DISTINCT Raca)
FROM tblPets AS p;

-- Select com AND e LIKE
SELECT *
FROM tblPets
WHERE Raca = 'SIAMES' AND Apelido LIKE 'C%';

-- Select com OR
SELECT *
FROM tblPets
WHERE Raca = 'SIAMES' OR Raca = 'ANGORA';

-- Select com OR e LIKE
SELECT *
FROM tblPets
WHERE Raca = 'SIAMES' OR Raca LIKE 'ANGORA';

-- Select com NOT LIKE
SELECT *
FROM tblPets
WHERE Raca NOT LIKE 'SIA%';

-- Select com TOP
SELECT TOP 3 *
FROM tblPets;


-- Select com MAX
SELECT MAX(Valor)
FROM tblPets;

-- Select com MIN
SELECT MIN(Valor)
FROM tblPets;

-- Select Between
SELECT *
FROM tblPets
WHERE Valor Between 1000 AND 2000;

-- Create View
CREATE VIEW minhaView AS
SELECT p.Apelido, p.Raca, p.Valor,
		a.Nome as Dono
FROM tblAlunos AS a, tblPets AS p
WHERE p.IdAluno = a.IdAluno;

-- Backup de banco
BACKUP DATABASE escola2
TO DISK = 'D:\bd\backup\backup1.bak';

-- Create trigger
CREATE TRIGGER aviso
ON tblPets
AFTER INSERT, UPDATE, DELETE  
AS RAISERROR ('Avisar o usuario', 16, 10);

-- teste o trigger
INSERT INTO tblPets ([Apelido],[Raca],[Valor]) VALUES('DOG5', 'FILA', 2300.00);


-- marca o banco de dados a ser usado
USE cafe

-- cria uma tabela com a LEDGER ligada
CREATE TABLE EntradaNoEdificio
(
   [IdFuncionario] INT NOT NULL,
   [EntradaNoEdificio] NVARCHAR (1024) NOT NULL,
   [Timestamp] Datetime2 NOT NULL
)
WITH (LEDGER = ON (APPEND_ONLY = ON));

-- Insere dados
INSERT INTO [EntradaNoEdificio] VALUES ('43869', 'Entrada_Edificio-42', '2020-05-02T19:58:47.1234567');
INSERT INTO [EntradaNoEdificio] VALUES ('43878', 'Entrada_Edificio-43', '2020-05-02T19:59:47.1234567');
INSERT INTO [EntradaNoEdificio] VALUES ('43869', 'Saida_Edificio-42', '2020-05-02T19:57:47.1234567');
INSERT INTO [EntradaNoEdificio] VALUES ('43845', 'Entrada_Edificio-41', '2020-05-02T19:56:47.1234567');

-- cria um bloco de transação T1
BEGIN TRAN T1;
	INSERT INTO [EntradaNoEdificio] VALUES ('11', 'Entrada_Edificio-73', '2020-05-02T19:53:47.1234567');
	INSERT INTO [EntradaNoEdificio] VALUES ('22', 'Entrada_-74', '2020-05-02T19:54:47.1234567');
	INSERT INTO [EntradaNoEdificio] VALUES ('11', 'Saida_Edificio-73', '2020-05-02T19:54:47.1234567');
COMMIT TRAN T1;

-- cria um bloco de transação T2
BEGIN TRAN T2;
	INSERT INTO [EntradaNoEdificio] VALUES ('44', 'Entrada_Edificio-43', '2020-05-02T19:53:47.1234567');
	INSERT INTO [EntradaNoEdificio] VALUES ('55', 'Entrada_Edificio-42', '2020-05-02T19:54:47.1234567');
	INSERT INTO [EntradaNoEdificio] VALUES ('55', 'Saida_Edificio-43', '2020-05-02T19:54:47.1234567');
COMMIT TRAN T2;

-- mostra o conteúdo da tabela
SELECT *,
	[ledger_start_transaction_id],
	[ledger_start_sequence_number]
FROM [EntradaNoEdificio];

-- mostra a estrutura da tabela ledger
SELECT
	t.[commit_time] AS [HoraCommit],
	t.[principal_name] AS [Usuario],
	l.[IdFuncionario],
	l.[EntradaNoEdificio],
	l.[Timestamp],
	l.[ledger_operation_type_desc] AS Operacao
FROM [EntradaNoEdificio_Ledger] l
JOIN sys.database_ledger_transactions t
	ON t.transaction_id = l.ledger_transaction_id
ORDER BY t.commit_time DESC;

-- uma variação do comando anterior
SELECT
	t.[commit_time] AS [HoraCommit],
	t.[principal_name] AS [Usuario], 
	l.[IdFuncionario],
	l.[EntradaNoEdificio],
	l.[Timestamp],
	l.[ledger_operation_type_desc] AS Operacao,
	l.ledger_transaction_id AS IdTransacao,
	l.ledger_sequence_number AS NumeroDeSequencia
FROM [EntradaNoEdificio_Ledger] l
JOIN sys.database_ledger_transactions t
	ON t.transaction_id = l.ledger_transaction_id
ORDER BY t.commit_time DESC;

-- tentativa de atualizar/alterar dados na tabela, DELETE e UPDATE não funcionam !
UPDATE EntradaNoEdificio SET IdFuncionario = 34184;

-- tentativa de deletar a tabela !
DELETE FROM EntradaNoEdificio;

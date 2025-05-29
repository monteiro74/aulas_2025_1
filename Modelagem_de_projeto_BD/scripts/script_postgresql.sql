// Comando para criar o banco de dados
CREATE DATABASE escola;

// criamos um esquema dentro do banco escola
CREATE SCHEMA academico;

// criamos um esquema dentro do banco escola
CREATE SCHEMA administrativo;

// comando para criar uma tabela dentro do esquema academico
CREATE TABLE academico.aluno (
    id SERIAL PRIMARY KEY,                       -- Inteiro autoincrementável
    matricula VARCHAR(10) UNIQUE NOT NULL,       -- Texto curto com restrição de unicidade
    nome TEXT NOT NULL,                          -- Texto de tamanho variável
    cpf CHAR(11) UNIQUE NOT NULL,                -- Texto fixo para CPF
    data_nascimento DATE NOT NULL,               -- Data
    idade INT,                                   -- Número inteiro
    email VARCHAR(100),                          -- E-mail (texto com limite)
    telefone VARCHAR(15),                        -- Número de telefone
    ativo BOOLEAN DEFAULT TRUE,                  -- Valor booleano
    peso NUMERIC(5,2),                           -- Número com precisão (ex: 70.50 kg)
    altura REAL,                                 -- Número de ponto flutuante simples
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Data e hora com padrão atual
);


// comando para criar uma tabela dentro do esquema academico
CREATE TABLE academico.professor (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    email VARCHAR(100),
    titulacao VARCHAR(50),
    data_admissao DATE
);

// comando para criar uma tabela dentro do esquema academico
CREATE TABLE academico.turma (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE NOT NULL,
    nome_disciplina TEXT NOT NULL,
    semestre VARCHAR(6), -- ex: 2025/1
    id_professor INT,
    FOREIGN KEY (id_professor) REFERENCES academico.professor(id)
);

// comando para criar uma tabela dentro do esquema academico
CREATE TABLE academico.aluno_turma (
    id_aluno INT NOT NULL,
    id_turma INT NOT NULL,
    data_matricula DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY (id_aluno, id_turma),
    FOREIGN KEY (id_aluno) REFERENCES academico.aluno(id),
    FOREIGN KEY (id_turma) REFERENCES academico.turma(id)
);

// Inserir dados fictícios na tabela professor
INSERT INTO academico.professor (nome, cpf, email, titulacao, data_admissao) VALUES
('Carlos Silva', '12345678900', 'carlos.silva@escola.edu.br', 'Mestre', '2015-02-10'),
('Ana Beatriz Costa', '98765432100', 'ana.costa@escola.edu.br', 'Doutora', '2018-08-15'),
('José Fernandes', '45612378900', 'jose.fernandes@escola.edu.br', 'Especialista', '2020-01-22');

// Inserir dados fictícios na tabela aluno
INSERT INTO academico.aluno (matricula, nome, cpf, data_nascimento, idade, email, telefone, ativo, peso, altura) VALUES
('A001', 'João Souza', '11111111111', '2002-01-15', 22, 'joao@escola.com', '65999990001', TRUE, 70.5, 1.75),
('A002', 'Mariana Lima', '22222222222', '2003-05-10', 21, 'mariana@escola.com', '65999990002', TRUE, 60.2, 1.62),
('A003', 'Pedro Henrique', '33333333333', '2004-07-25', 20, 'pedro@escola.com', '65999990003', TRUE, 68.0, 1.78),
('A004', 'Luciana Alves', '44444444444', '2001-09-30', 23, 'luciana@escola.com', '65999990004', TRUE, 55.0, 1.68),
('A005', 'Bruno Teixeira', '55555555555', '2005-02-14', 19, 'bruno@escola.com', '65999990005', TRUE, 80.0, 1.82);

// Inserir dados na tabela turmas
-- Assume que os IDs dos professores são 1, 2, 3 (baseado na ordem de inserção)
INSERT INTO academico.turma (codigo, nome_disciplina, semestre, id_professor) VALUES
('TURMA01', 'Matemática Aplicada', '2025/1', 1),
('TURMA02', 'Física I', '2025/1', 2),
('TURMA03', 'Química Geral', '2025/1', 3),
('TURMA04', 'Algoritmos', '2025/1', 1);

// Inserir dados na tabela que vincula aluno<-->turma
-- Aluno A001 em 2 turmas
INSERT INTO academico.aluno_turma (id_aluno, id_turma) VALUES
(1, 1), -- João → Matemática
(1, 2); -- João → Física

-- Aluno A002 em 1 turma
INSERT INTO academico.aluno_turma (id_aluno, id_turma) VALUES
(2, 1); -- Mariana → Matemática

-- Aluno A003 em 3 turmas
INSERT INTO academico.aluno_turma (id_aluno, id_turma) VALUES
(3, 1),
(3, 2),
(3, 3);

-- Aluno A004 em 1 turma
INSERT INTO academico.aluno_turma (id_aluno, id_turma) VALUES
(4, 4);

-- Aluno A005 em 2 turmas
INSERT INTO academico.aluno_turma (id_aluno, id_turma) VALUES
(5, 3),
(5, 4);

// Consultas básicas:
// Listar alunos por turma
// Listar turmas de um professor
// Contar alunos por turma

// os alunos por turma (com nome da turma)
SELECT
  t.codigo AS codigo_turma,
  t.nome_disciplina,
  a.nome AS nome_aluno,
  a.matricula
FROM
  academico.aluno_turma at
JOIN academico.aluno a ON at.id_aluno = a.id
JOIN academico.turma t ON at.id_turma = t.id
ORDER BY t.codigo, a.nome;


// turmas de um professor (por nome)
SELECT
  p.nome AS nome_professor,
  t.codigo AS codigo_turma,
  t.nome_disciplina,
  t.semestre
FROM
  academico.turma t
JOIN academico.professor p ON t.id_professor = p.id
ORDER BY p.nome, t.codigo;

// número de alunos em cada turma
SELECT
  t.codigo AS codigo_turma,
  t.nome_disciplina,
  COUNT(at.id_aluno) AS total_alunos
FROM
  academico.turma t
LEFT JOIN academico.aluno_turma at ON t.id = at.id_turma
GROUP BY t.id, t.codigo, t.nome_disciplina
ORDER BY total_alunos DESC;


-- ---------------------------------------------------------------
-- Script SQL para copiar dados do banco_origem para o banco_destino
-- o banco_destino tem um modelo snowflake
-- ---------------------------------------------------------------


-- Criando a tabela de endereço (auxiliar para lojas1)
CREATE TABLE endereco_lojas1 (
    id_endereco_loja INT PRIMARY KEY,
    rua VARCHAR(100),
    cidade VARCHAR(50),
    estado VARCHAR(50),
    cep VARCHAR(10)
);

-- Tabela: lojas1
CREATE TABLE lojas1 (
    id_loja INT PRIMARY KEY,
    numero_da_loja VARCHAR(20),
    id_endereco_loja INT,
    FOREIGN KEY (id_endereco_loja) REFERENCES endereco_lojas1(id_endereco_loja)
);

-- Tabela: produtos1
CREATE TABLE produtos1 (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    marca_produto VARCHAR(50),
    fornecedor_produto VARCHAR(50),
    categoria_produto VARCHAR(50)
);

-- Tabela: vendas1
CREATE TABLE vendas1 (
    id_data DATE,
    id_loja INT,
    id_produto INT,
    unidades_vendidas INT,
    valor_total DECIMAL(10,2),
    PRIMARY KEY (id_data, id_loja, id_produto),
    FOREIGN KEY (id_loja) REFERENCES lojas1(id_loja),
    FOREIGN KEY (id_produto) REFERENCES produtos1(id_produto)
);

-- Inserindo dados fictícios

-- Endereços
INSERT INTO endereco_lojas1 (id_endereco_loja, rua, cidade, estado, cep) VALUES
(1, 'Rua A, 123', 'São Paulo', 'SP', '01000-000'),
(2, 'Av. B, 456', 'Rio de Janeiro', 'RJ', '20000-000'),
(3, 'Rua C, 789', 'Belo Horizonte', 'MG', '30000-000'),
(4, 'Av. D, 101', 'Curitiba', 'PR', '80000-000'),
(5, 'Rua E, 202', 'Porto Alegre', 'RS', '90000-000');

-- Lojas
INSERT INTO lojas1 (id_loja, numero_da_loja, id_endereco_loja) VALUES
(1, 'LJ001', 1),
(2, 'LJ002', 2),
(3, 'LJ003', 3),
(4, 'LJ004', 4),
(5, 'LJ005', 5);

-- Produtos
INSERT INTO produtos1 (id_produto, nome_produto, marca_produto, fornecedor_produto, categoria_produto) VALUES
(1, 'Smartphone X', 'TechBrand', 'Fornecedor A', 'Eletrônicos'),
(2, 'Notebook Pro', 'NoteCo', 'Fornecedor B', 'Informática'),
(3, 'TV 50"', 'VisionTV', 'Fornecedor C', 'Eletrônicos'),
(4, 'Fone de Ouvido', 'SoundMax', 'Fornecedor A', 'Acessórios'),
(5, 'Mouse Gamer', 'GameTech', 'Fornecedor B', 'Informática');

-- Vendas
INSERT INTO vendas1 (id_data, id_loja, id_produto, unidades_vendidas, valor_total) VALUES
('2025-04-01', 1, 1, 10, 5000.00),
('2025-04-01', 2, 2, 5, 12500.00),
('2025-04-02', 3, 3, 3, 7500.00),
('2025-04-03', 4, 4, 15, 1500.00),
('2025-04-03', 5, 5, 7, 1050.00);


-- criar o novo modelo ----------------

-- Dimensão de tempo
CREATE TABLE dim_data (
    id_data DATE PRIMARY KEY,
    dia INT,
    dia_semana VARCHAR(20),
    semana_mes INT,
    mes INT,
    ano INT
);

-- Dimensão de localização da loja
CREATE TABLE dim_local (
    id_local INT PRIMARY KEY,
    rua VARCHAR(100),
    cidade VARCHAR(50),
    estado VARCHAR(50),
    cep VARCHAR(10)
);

-- Dimensão loja, com chave para localização
CREATE TABLE dim_loja (
    id_loja INT PRIMARY KEY,
    numero_loja VARCHAR(20),
    id_local INT,
    FOREIGN KEY (id_local) REFERENCES dim_local(id_local)
);

-- Dimensão de marca
CREATE TABLE dim_marca (
    id_marca INT PRIMARY KEY,
    nome_marca VARCHAR(50)
);

-- Dimensão de fornecedor
CREATE TABLE dim_fornecedor (
    id_fornecedor INT PRIMARY KEY,
    nome_fornecedor VARCHAR(50)
);

-- Dimensão de categoria
CREATE TABLE dim_categoria (
    id_categoria INT PRIMARY KEY,
    nome_categoria VARCHAR(50)
);

-- Dimensão de produtos com referências às dimensões relacionadas
CREATE TABLE dim_produtos (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    id_marca INT,
    id_fornecedor INT,
    id_categoria INT,
    FOREIGN KEY (id_marca) REFERENCES dim_marca(id_marca),
    FOREIGN KEY (id_fornecedor) REFERENCES dim_fornecedor(id_fornecedor),
    FOREIGN KEY (id_categoria) REFERENCES dim_categoria(id_categoria)
);


--  Inserir na dim_data (removendo duplicatas da vendas1)

INSERT INTO banco_destino.dim_data (id_data, dia, dia_semana, semana_mes, mes, ano)
SELECT DISTINCT 
    id_data,
    DAY(id_data) AS dia,
    DAYNAME(id_data) AS dia_semana,
    FLOOR((DAY(id_data)-1)/7) + 1 AS semana_mes,
    MONTH(id_data) AS mes,
    YEAR(id_data) AS ano
FROM banco_origem.vendas1;



-- Inserir na dim_local
INSERT INTO banco_destino.dim_local (id_local, rua, cidade, estado, cep)
SELECT DISTINCT
    el.id_endereco_loja,
    el.rua,
    el.cidade,
    el.estado,
    el.cep
FROM banco_origem.endereco_lojas1 el;

-- Inserir na dim_loja
INSERT INTO banco_destino.dim_loja (id_loja, numero_loja, id_local)
SELECT DISTINCT
    l.id_loja,
    l.numero_da_loja,
    l.id_endereco_loja
FROM banco_origem.lojas1 l;

-- Inserir nas tabelas de domínio: dim_marca, dim_fornecedor, dim_categoria

-- Marca
INSERT INTO banco_destino.dim_marca (id_marca, nome_marca)
SELECT DISTINCT
    ROW_NUMBER() OVER (ORDER BY marca_produto) AS id_marca,
    marca_produto
FROM banco_origem.produtos1;

-- Fornecedor
INSERT INTO banco_destino.dim_fornecedor (id_fornecedor, nome_fornecedor)
SELECT DISTINCT
    ROW_NUMBER() OVER (ORDER BY fornecedor_produto) AS id_fornecedor,
    fornecedor_produto
FROM banco_origem.produtos1;

-- Categoria
INSERT INTO banco_destino.dim_categoria (id_categoria, nome_categoria)
SELECT DISTINCT
    ROW_NUMBER() OVER (ORDER BY categoria_produto) AS id_categoria,
    categoria_produto
FROM banco_origem.produtos1;


-- Inserir na dim_produtos
-- INSERT IGNORE para ignorar duplicatas com base na PK (id_produto):
INSERT IGNORE INTO banco_destino.dim_produtos (id_produto, nome_produto, id_marca, id_fornecedor, id_categoria)
SELECT
    p.id_produto,
    p.nome_produto,
    m.id_marca,
    f.id_fornecedor,
    c.id_categoria
FROM banco_origem.produtos1 p
JOIN banco_destino.dim_marca m ON p.marca_produto = m.nome_marca
JOIN banco_destino.dim_fornecedor f ON p.fornecedor_produto = f.nome_fornecedor
JOIN banco_destino.dim_categoria c ON p.categoria_produto = c.nome_categoria;

ou

-- sobrescrever o registro caso ele já exista:
INSERT INTO dim_produtos (id_produto, nome_produto, id_marca, id_fornecedor, id_categoria)
SELECT
    p.id_produto,
    p.nome_produto,
    m.id_marca,
    f.id_fornecedor,
    c.id_categoria
FROM banco_origem.produtos1 p
JOIN dim_marca m ON p.marca_produto = m.nome_marca
JOIN dim_fornecedor f ON p.fornecedor_produto = f.nome_fornecedor
JOIN dim_categoria c ON p.categoria_produto = c.nome_categoria
ON DUPLICATE KEY UPDATE
    nome_produto = VALUES(nome_produto),
    id_marca = VALUES(id_marca),
    id_fornecedor = VALUES(id_fornecedor),
    id_categoria = VALUES(id_categoria);
    
   


# --- Cria o banco --------------------------------------------

CREATE DATABASE banco1

CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(255),
    categoria VARCHAR(255),
    marca VARCHAR(255)
);

CREATE TABLE lojas (
    id_loja INT AUTO_INCREMENT PRIMARY KEY,
    nome_loja VARCHAR(255),
    localizacao VARCHAR(255)
);

CREATE TABLE vendedores (
    id_vendedor INT AUTO_INCREMENT PRIMARY KEY,
    nome_vendedor VARCHAR(255),
    regiao VARCHAR(255)
);

CREATE TABLE datas (
    id_data INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    mes INT,
    trimestre INT,
    ano INT,
    dia_da_semana INT
);

CREATE TABLE vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_vendedor INT,
    id_loja INT,
    data DATE,
    valor_total_venda DECIMAL(10, 2),
    FOREIGN KEY (id_vendedor) REFERENCES vendedores(id_vendedor),
    FOREIGN KEY (id_loja) REFERENCES lojas(id_loja)
);


CREATE TABLE item_vendas (
    id_item_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_venda INT,
    id_produto INT,
    quantidade_vendida INT,
    preco_unitario DECIMAL(10, 2),
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (id_venda) REFERENCES vendas(id_venda),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);






# --- Insere dados no banco OLTP --------------------------------------------

INSERT INTO lojas (nome_loja, localizacao) VALUES
('Loja Centro', 'Centro da Cidade'),
('Loja Shopping', 'Shopping Mall'),
('Loja Bairro Norte', 'Bairro Norte'),
('Loja Bairro Sul', 'Bairro Sul'),
('Loja Online', 'Internet'),
('Loja Grande', 'Av. Principal'),
('Loja Pequena', 'Rua Secundária'),
('Loja Fast', 'Shopping Rápido'),
('Loja Premium', 'Centro Comercial'),
('Loja Express', 'Praça de Alimentação');

INSERT INTO produtos (nome_produto, categoria, marca) VALUES
('Smartphone X1', 'Eletrônicos', 'BrandA'),
('Laptop Y2', 'Eletrônicos', 'BrandB'),
('Camiseta Polo', 'Roupas', 'BrandC'),
('Tênis Esportivo', 'Calçados', 'BrandD'),
('Cafeteira Automática', 'Eletrodomésticos', 'BrandE'),
('Relógio Inteligente', 'Acessórios', 'BrandF'),
('Fones de Ouvido Bluetooth', 'Acessórios', 'BrandG'),
('Cadeira Ergonomica', 'Móveis', 'BrandH'),
('Mesa de Jantar', 'Móveis', 'BrandI'),
('Câmera Digital', 'Fotografia', 'BrandJ');

INSERT INTO vendedores (nome_vendedor, regiao) VALUES
('Ana Oliveira', 'Centro'),
('Carlos Souza', 'Norte'),
('Fernanda Lima', 'Sul'),
('João Pereira', 'Leste'),
('Maria Silva', 'Oeste'),
('Luiz Santos', 'Centro'),
('Patrícia Costa', 'Sul'),
('Rafael Almeida', 'Norte'),
('Beatriz Rocha', 'Leste'),
('Gustavo Martins', 'Oeste');

INSERT INTO vendas (id_vendedor, id_loja, data, valor_total_venda) VALUES
(1, 1, '2025-03-01', 1500.00),  -- Venda em 01 de março de 2025
(2, 2, '2025-03-02', 2000.00),  -- Venda em 02 de março de 2025
(3, 3, '2025-03-03', 800.00),   -- Venda em 03 de março de 2025
(4, 4, '2025-03-04', 1200.00),  -- Venda em 04 de março de 2025
(5, 5, '2025-03-05', 1800.00),  -- Venda em 05 de março de 2025
(6, 6, '2025-03-06', 1000.00),  -- Venda em 06 de março de 2025
(7, 7, '2025-03-07', 2200.00),  -- Venda em 07 de março de 2025
(8, 8, '2025-03-08', 900.00),   -- Venda em 08 de março de 2025
(9, 9, '2025-03-09', 1700.00),  -- Venda em 09 de março de 2025
(10, 10, '2025-03-10', 1100.00); -- Venda em 10 de março de 2025


INSERT INTO item_vendas (id_venda, id_produto, quantidade_vendida, preco_unitario, valor_total) VALUES
(1, 1, 1, 1000.00, 1000.00),  -- Produto 1 na venda 1
(1, 3, 2, 250.00, 500.00),    -- Produto 3 na venda 1
(2, 2, 1, 1200.00, 1200.00), -- Produto 2 na venda 2
(2, 6, 2, 400.00, 800.00),   -- Produto 6 na venda 2
(3, 4, 1, 300.00, 300.00),   -- Produto 4 na venda 3
(3, 9, 1, 500.00, 500.00),   -- Produto 9 na venda 3
(4, 5, 1, 500.00, 500.00),   -- Produto 5 na venda 4
(4, 7, 1, 700.00, 700.00),   -- Produto 7 na venda 4
(5, 8, 1, 400.00, 400.00),   -- Produto 8 na venda 5
(5, 10, 2, 700.00, 1400.00), -- Produto 10 na venda 5
(6, 6, 1, 400.00, 400.00),   -- Produto 6 na venda 6
(6, 2, 1, 1200.00, 1200.00), -- Produto 2 na venda 6
(7, 3, 2, 250.00, 500.00),   -- Produto 3 na venda 7
(8, 4, 1, 300.00, 300.00),   -- Produto 4 na venda 8
(9, 5, 1, 500.00, 500.00),   -- Produto 5 na venda 9
(9, 8, 2, 400.00, 800.00),   -- Produto 8 na venda 9
(10, 6, 1, 400.00, 400.00),  -- Produto 6 na venda 10
(10, 9, 1, 500.00, 500.00);  -- Produto 9 na venda 10







# --- Cria uma tabela Dimensão para datas únicas --------------------------------------------

INSERT INTO datas (data, mes, trimestre, ano, dia_da_semana)
SELECT DISTINCT
    v.data,
    MONTH(v.data) AS mes,
    QUARTER(v.data) AS trimestre,
    YEAR(v.data) AS ano,
    DAYOFWEEK(v.data) AS dia_da_semana
FROM vendas v
WHERE NOT EXISTS (
    SELECT 1
    FROM datas d
    WHERE d.data = v.data
);






# --- Exemplo de select: mostra soma de vendas por agrupadas por vendedor --------------------------------------------

SELECT 
    vd.nome_vendedor, 
    SUM(iv.valor_total) AS total_vendas
FROM 
    item_vendas iv
JOIN 
    vendas v ON iv.id_venda = v.id_venda
JOIN 
    vendedores vd ON v.id_vendedor = vd.id_vendedor
JOIN 
    datas d ON v.data = d.data
WHERE 
    d.mes = 3 AND d.ano = 2025
GROUP BY 
    vd.nome_vendedor;


	
	
	
	
	
# --- Exemplo de select: mostra soma de vendas por agrupadas por produto --------------------------------------------


SELECT 
    p.nome_produto,
    SUM(iv.quantidade_vendida) AS quantidade_total_vendida
FROM 
    item_vendas iv
JOIN 
    produtos p ON iv.id_produto = p.id_produto
JOIN 
    vendas v ON iv.id_venda = v.id_venda
JOIN 
    datas d ON v.data = d.data
WHERE 
    d.ano = 2025
GROUP BY 
    p.nome_produto
ORDER BY 
    quantidade_total_vendida DESC;

	
	
	
	
	
	
# --- Cria uma view que une as tabelas vendas e itens de vendas --------------------------------------------

	
CREATE VIEW vw_vendas_itens AS
SELECT 
    v.id_venda,
    v.id_vendedor,
    v.id_loja,
    v.data AS data_venda,
    v.valor_total_venda,
    iv.id_item_venda,
    iv.id_produto,
    iv.quantidade_vendida,
    iv.preco_unitario,
    iv.valor_total AS valor_item_venda
FROM 
    vendas v
JOIN 
    item_vendas iv ON v.id_venda = iv.id_venda;


	
	

# --- Cria um view que une TODAS as tabelas ---------------------------------------------------------

CREATE VIEW vw_vendas_completas AS
SELECT 
    v.id_venda,
    v.data AS data_venda,
    d.mes,
    d.trimestre,
    d.ano,
    d.dia_da_semana,
    v.valor_total_venda,
    ven.id_vendedor,
    ven.nome_vendedor,
    ven.regiao AS regiao_vendedor,
    l.id_loja,
    l.nome_loja,
    l.localizacao AS localizacao_loja,
    p.id_produto,
    p.nome_produto,
    p.categoria,
    p.marca,
    iv.quantidade_vendida,
    iv.preco_unitario,
    iv.valor_total AS valor_item_venda
FROM 
    vendas v
JOIN 
    vendedores ven ON v.id_vendedor = ven.id_vendedor
JOIN 
    lojas l ON v.id_loja = l.id_loja
JOIN 
    datas d ON v.data = d.data
JOIN 
    item_vendas iv ON v.id_venda = iv.id_venda
JOIN 
    produtos p ON iv.id_produto = p.id_produto;

	
	
	
	
# --- Criação de indices para acelerar a view acima ------------------------------------

CREATE INDEX idx_vendas_vendedor ON vendas(id_vendedor);
CREATE INDEX idx_vendas_loja ON vendas(id_loja);
CREATE INDEX idx_vendas_data ON vendas(data);
CREATE INDEX idx_item_vendas_venda ON item_vendas(id_venda);
CREATE INDEX idx_item_vendas_produto ON item_vendas(id_produto);
CREATE INDEX idx_produtos_produto ON produtos(id_produto);
CREATE INDEX idx_lojas_loja ON lojas(id_loja);
CREATE INDEX idx_vendedores_vendedor ON vendedores(id_vendedor);





# --- Explicar o plano de execução da consulta -------------------------

EXPLAIN SELECT * FROM vw_vendas_completas;





# --- Cria uma tabela temporária com o resultado da view -----------------------

CREATE TABLE vendas_completas_temp AS
SELECT * FROM vw_vendas_completas;






# --- Cria uma view com "Limit" ---------------------------------------------

create or replace
algorithm = UNDEFINED view `vw_vendas_completas_limit5` as
select
    `v`.`id_venda` as `id_venda`,
    `v`.`data` as `data_venda`,
    `d`.`mes` as `mes`,
    `d`.`trimestre` as `trimestre`,
    `d`.`ano` as `ano`,
    `d`.`dia_da_semana` as `dia_da_semana`,
    `v`.`valor_total_venda` as `valor_total_venda`,
    `ven`.`id_vendedor` as `id_vendedor`,
    `ven`.`nome_vendedor` as `nome_vendedor`,
    `ven`.`regiao` as `regiao_vendedor`,
    `l`.`id_loja` as `id_loja`,
    `l`.`nome_loja` as `nome_loja`,
    `l`.`localizacao` as `localizacao_loja`,
    `p`.`id_produto` as `id_produto`,
    `p`.`nome_produto` as `nome_produto`,
    `p`.`categoria` as `categoria`,
    `p`.`marca` as `marca`,
    `iv`.`quantidade_vendida` as `quantidade_vendida`,
    `iv`.`preco_unitario` as `preco_unitario`,
    `iv`.`valor_total` as `valor_item_venda`
from
    (((((`vendas` `v`
join `vendedores` `ven` on
    ((`v`.`id_vendedor` = `ven`.`id_vendedor`)))
join `lojas` `l` on
    ((`v`.`id_loja` = `l`.`id_loja`)))
join `datas` `d` on
    ((`v`.`data` = `d`.`data`)))
join `item_vendas` `iv` on
    ((`v`.`id_venda` = `iv`.`id_venda`)))
join `produtos` `p` on
    ((`iv`.`id_produto` = `p`.`id_produto`)))
limit 5;



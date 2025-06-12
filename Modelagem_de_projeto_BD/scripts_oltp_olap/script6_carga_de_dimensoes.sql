-- Popula dw_dim_cidade
INSERT INTO dw_dim_cidade (id_cidade, nome, estado)
SELECT id_cidade, nome, estado
FROM cidades;

-- Popula dw_dim_cliente
INSERT INTO dw_dim_cliente (id_cliente, nome, email, id_cidade)
SELECT id_cliente, nome, email, id_cidade
FROM clientes;

-- Popula dw_dim_categoria
INSERT INTO dw_dim_categoria (id_categoria, nome)
SELECT id_categoria, nome
FROM categorias;

-- Popula dw_dim_fornecedor
INSERT INTO dw_dim_fornecedor (id_fornecedor, nome, id_cidade)
SELECT id_fornecedor, nome, id_cidade
FROM fornecedores;

-- Popula dw_dim_loja
INSERT INTO dw_dim_loja (id_loja, nome, id_cidade)
SELECT id_loja, nome, id_cidade
FROM lojas;

-- Popula dw_dim_produto
INSERT INTO dw_dim_produto (id_produto, nome, id_categoria, id_fornecedor, preco)
SELECT id_produto, nome, id_categoria, id_fornecedor, preco
FROM produtos;

-- Popula dw_dim_vendedor
INSERT INTO dw_dim_vendedor (id_vendedor, nome, id_loja)
SELECT id_vendedor, nome, id_loja
FROM vendedores;

-- Popula dw_dim_tempo (datas únicas das vendas)
INSERT INTO dw_dim_tempo (data, ano, trimestre, mes, dia, dia_semana)
SELECT DISTINCT
    data,
    YEAR(data) AS ano,
    QUARTER(data) AS trimestre,
    MONTH(data) AS mes,
    DAY(data) AS dia,
    DAYNAME(data) AS dia_semana
FROM vendas;

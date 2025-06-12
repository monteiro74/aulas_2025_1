
-- Dimensão Tempo
CREATE TABLE dw_dim_tempo (
    id_tempo INT PRIMARY KEY AUTO_INCREMENT,
    data DATE,
    ano INT,
    trimestre INT,
    mes INT,
    dia INT,
    dia_semana VARCHAR(15)
);

-- Dimensão Cliente
CREATE TABLE dw_dim_cliente (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    id_cidade INT
);

-- Dimensão Produto
CREATE TABLE dw_dim_produto (
    id_produto INT PRIMARY KEY,
    nome VARCHAR(100),
    id_categoria INT,
    id_fornecedor INT,
    preco DECIMAL(10,2)
);

-- Dimensão Categoria
CREATE TABLE dw_dim_categoria (
    id_categoria INT PRIMARY KEY,
    nome VARCHAR(100)
);

-- Dimensão Fornecedor
CREATE TABLE dw_dim_fornecedor (
    id_fornecedor INT PRIMARY KEY,
    nome VARCHAR(100),
    id_cidade INT
);

-- Dimensão Loja
CREATE TABLE dw_dim_loja (
    id_loja INT PRIMARY KEY,
    nome VARCHAR(100),
    id_cidade INT
);

-- Dimensão Vendedor
CREATE TABLE dw_dim_vendedor (
    id_vendedor INT PRIMARY KEY,
    nome VARCHAR(100),
    id_loja INT
);

-- Dimensão Cidade
CREATE TABLE dw_dim_cidade (
    id_cidade INT PRIMARY KEY,
    nome VARCHAR(100),
    estado VARCHAR(2)
);

-- Tabela Fato Vendas (Grão: item de venda)
CREATE TABLE dw_fato_vendas (
    id_fato INT PRIMARY KEY AUTO_INCREMENT,
    id_tempo INT,
    id_cliente INT,
    id_produto INT,
    id_categoria INT,
    id_fornecedor INT,
    id_loja INT,
    id_vendedor INT,
    id_cidade_loja INT,
    id_cidade_cliente INT,
    id_cidade_fornecedor INT,
    quantidade INT,
    preco_unitario DECIMAL(10,2),
    preco_total DECIMAL(12,2),
    FOREIGN KEY (id_tempo) REFERENCES dw_dim_tempo(id_tempo),
    FOREIGN KEY (id_cliente) REFERENCES dw_dim_cliente(id_cliente),
    FOREIGN KEY (id_produto) REFERENCES dw_dim_produto(id_produto),
    FOREIGN KEY (id_categoria) REFERENCES dw_dim_categoria(id_categoria),
    FOREIGN KEY (id_fornecedor) REFERENCES dw_dim_fornecedor(id_fornecedor),
    FOREIGN KEY (id_loja) REFERENCES dw_dim_loja(id_loja),
    FOREIGN KEY (id_vendedor) REFERENCES dw_dim_vendedor(id_vendedor),
    FOREIGN KEY (id_cidade_loja) REFERENCES dw_dim_cidade(id_cidade),
    FOREIGN KEY (id_cidade_cliente) REFERENCES dw_dim_cidade(id_cidade),
    FOREIGN KEY (id_cidade_fornecedor) REFERENCES dw_dim_cidade(id_cidade)
);

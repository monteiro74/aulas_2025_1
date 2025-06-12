
--- Comandos SQL `CREATE TABLE` para MySQL

```sql
CREATE TABLE cidades (
    id_cidade INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    estado VARCHAR(2) NOT NULL
);

CREATE TABLE lojas (
    id_loja INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    id_cidade INT NOT NULL,
    FOREIGN KEY (id_cidade) REFERENCES cidades(id_cidade)
);

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    id_cidade INT NOT NULL,
    FOREIGN KEY (id_cidade) REFERENCES cidades(id_cidade)
);

CREATE TABLE fornecedores (
    id_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    id_cidade INT NOT NULL,
    FOREIGN KEY (id_cidade) REFERENCES cidades(id_cidade)
);

CREATE TABLE categorias (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE produtos (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    id_categoria INT NOT NULL,
    id_fornecedor INT NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL DEFAULT 0,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id_fornecedor)
);

CREATE TABLE vendedores (
    id_vendedor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    id_loja INT NOT NULL,
    FOREIGN KEY (id_loja) REFERENCES lojas(id_loja)
);

CREATE TABLE vendas (
    id_venda INT PRIMARY KEY AUTO_INCREMENT,
    data DATE NOT NULL,
    valor_total DECIMAL(12,2) NOT NULL,
    id_loja INT NOT NULL,
    id_cliente INT NOT NULL,
    id_vendedor INT NOT NULL,
    FOREIGN KEY (id_loja) REFERENCES lojas(id_loja),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_vendedor) REFERENCES vendedores(id_vendedor)
);

CREATE TABLE itens_venda (
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    id_venda INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    preco_total DECIMAL(12,2) NOT NULL,
    FOREIGN KEY (id_venda) REFERENCES vendas(id_venda),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);


--- Comandos SQL `INSERT` para popular tabelas

INSERT INTO cidades (nome, estado) VALUES
('São Paulo', 'SP'),
('Rio de Janeiro', 'RJ'),
('Belo Horizonte', 'MG'),
('Curitiba', 'PR'),
('Salvador', 'BA'),
('Porto Alegre', 'RS'),
('Brasília', 'DF'),
('Manaus', 'AM'),
('Recife', 'PE'),
('Goiânia', 'GO');


INSERT INTO categorias (nome) VALUES
('Eletrônicos'),
('Alimentos'),
('Vestuário'),
('Móveis'),
('Livros'),
('Informática'),
('Brinquedos'),
('Beleza'),
('Esportes'),
('Ferramentas');


INSERT INTO clientes (nome, email, id_cidade) VALUES
('João da Silva', 'joao.silva@email.com', 1),
('Maria Oliveira', 'maria.oliveira@email.com', 2),
('Ana Santos', 'ana.santos@email.com', 3),
('Pedro Souza', 'pedro.souza@email.com', 4),
('Carla Almeida', 'carla.almeida@email.com', 5),
('Lucas Lima', 'lucas.lima@email.com', 6),
('Bruno Pereira', 'bruno.pereira@email.com', 7),
('Patrícia Mendes', 'patricia.mendes@email.com', 8),
('Felipe Costa', 'felipe.costa@email.com', 9),
('Letícia Dias', 'leticia.dias@email.com', 10);


INSERT INTO fornecedores (nome, id_cidade) VALUES
('GlobalTech', 1),
('AlimBrasil', 2),
('ModaFácil', 3),
('MoveisCenter', 4),
('BookWorld', 5),
('InfoStore', 6),
('BrinqueBem', 7),
('BelezaPura', 8),
('SportLife', 9),
('FerramentasPro', 10);


INSERT INTO lojas (nome, id_cidade) VALUES
('Loja Central', 1),
('Mega Store', 2),
('Super Compras', 3),
('Ponto Certo', 4),
('Shopping Fácil', 5),
('Casa Nova', 6),
('Mundo Kids', 7),
('Top Moda', 8),
('Esporte Total', 9),
('Utilidades', 10);

INSERT INTO produtos (nome, id_categoria, id_fornecedor, preco, estoque) VALUES
('Smartphone', 1, 1, 1999.99, 50),
('Arroz 5kg', 2, 2, 22.50, 200),
('Camiseta Básica', 3, 3, 39.90, 150),
('Sofá 3 Lugares', 4, 4, 1499.00, 20),
('Livro de Romance', 5, 5, 49.90, 100),
('Notebook', 6, 6, 3499.99, 30),
('Boneca Baby', 7, 7, 79.90, 60),
('Perfume Floral', 8, 8, 120.00, 80),
('Bola de Futebol', 9, 9, 89.90, 75),
('Furadeira', 10, 10, 299.90, 40);



INSERT INTO vendedores (nome, id_loja) VALUES
('André Moraes', 1),
('Bianca Silva', 2),
('Carlos Souza', 3),
('Daniela Lima', 4),
('Eduardo Ramos', 5),
('Fernanda Torres', 6),
('Gustavo Pires', 7),
('Helena Costa', 8),
('Igor Martins', 9),
('Juliana Nunes', 10);




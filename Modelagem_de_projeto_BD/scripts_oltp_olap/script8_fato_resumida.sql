CREATE TABLE dw_fato_venda_resumida (
    id_fato INT PRIMARY KEY AUTO_INCREMENT,
    id_tempo INT,
    id_cliente INT,
    id_loja INT,
    id_vendedor INT,
    id_cidade_loja INT,
    id_cidade_cliente INT,
    quantidade_total INT,
    valor_total DECIMAL(12,2),
    FOREIGN KEY (id_tempo) REFERENCES dw_dim_tempo(id_tempo),
    FOREIGN KEY (id_cliente) REFERENCES dw_dim_cliente(id_cliente),
    FOREIGN KEY (id_loja) REFERENCES dw_dim_loja(id_loja),
    FOREIGN KEY (id_vendedor) REFERENCES dw_dim_vendedor(id_vendedor),
    FOREIGN KEY (id_cidade_loja) REFERENCES dw_dim_cidade(id_cidade),
    FOREIGN KEY (id_cidade_cliente) REFERENCES dw_dim_cidade(id_cidade)
);

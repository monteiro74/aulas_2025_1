INSERT INTO dw_fato_vendas (
    id_tempo, id_cliente, id_produto, id_categoria, id_fornecedor,
    id_loja, id_vendedor, id_cidade_loja, id_cidade_cliente, id_cidade_fornecedor,
    quantidade, preco_unitario, preco_total
)
SELECT
    t.id_tempo,
    v.id_cliente,
    p.id_produto,
    p.id_categoria,
    p.id_fornecedor,
    v.id_loja,
    v.id_vendedor,
    l.id_cidade AS id_cidade_loja,
    c.id_cidade AS id_cidade_cliente,
    f.id_cidade AS id_cidade_fornecedor,
    iv.quantidade,
    iv.preco_unitario,
    iv.preco_total
FROM itens_venda iv
JOIN vendas v             ON iv.id_venda = v.id_venda
JOIN produtos p           ON iv.id_produto = p.id_produto
JOIN fornecedores f       ON p.id_fornecedor = f.id_fornecedor
JOIN clientes c           ON v.id_cliente = c.id_cliente
JOIN lojas l              ON v.id_loja = l.id_loja
JOIN dw_dim_tempo t       ON v.data = t.data;

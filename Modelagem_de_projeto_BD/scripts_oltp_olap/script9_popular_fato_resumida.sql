INSERT INTO dw_fato_venda_resumida (
    id_tempo, id_cliente, id_loja, id_vendedor,
    id_cidade_loja, id_cidade_cliente,
    quantidade_total, valor_total
)
SELECT
    t.id_tempo,
    v.id_cliente,
    v.id_loja,
    v.id_vendedor,
    l.id_cidade AS id_cidade_loja,
    c.id_cidade AS id_cidade_cliente,
    SUM(iv.quantidade) AS quantidade_total,
    v.valor_total
FROM vendas v
JOIN dw_dim_tempo t   ON v.data = t.data
JOIN clientes c       ON v.id_cliente = c.id_cliente
JOIN lojas l          ON v.id_loja = l.id_loja
JOIN itens_venda iv   ON v.id_venda = iv.id_venda
GROUP BY v.id_venda;

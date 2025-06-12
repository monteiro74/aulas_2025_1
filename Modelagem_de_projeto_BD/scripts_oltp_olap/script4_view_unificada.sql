CREATE OR REPLACE VIEW vw_vendas_completas AS
SELECT
    v.id_venda                    AS venda_id,
    v.data                        AS data_venda,
    v.valor_total                 AS valor_total_venda,

    -- Loja
    l.id_loja                     AS loja_id,
    l.nome                        AS loja_nome,
    cl_loja.nome                  AS cidade_loja_nome,
    cl_loja.estado                AS cidade_loja_estado,

    -- Vendedor
    vend.id_vendedor              AS vendedor_id,
    vend.nome                     AS vendedor_nome,

    -- Cliente
    c.id_cliente                  AS cliente_id,
    c.nome                        AS cliente_nome,
    c.email                       AS cliente_email,
    cl_cli.nome                   AS cidade_cliente_nome,
    cl_cli.estado                 AS cidade_cliente_estado,

    -- Item de Venda
    iv.id_item                    AS item_id,
    iv.quantidade                 AS item_quantidade,
    iv.preco_unitario             AS item_preco_unitario,
    iv.preco_total                AS item_preco_total,

    -- Produto
    p.id_produto                  AS produto_id,
    p.nome                        AS produto_nome,
    p.preco                       AS produto_preco,
    p.estoque                     AS produto_estoque,

    -- Categoria do Produto
    cat.id_categoria              AS categoria_id,
    cat.nome                      AS categoria_nome,

    -- Fornecedor
    f.id_fornecedor               AS fornecedor_id,
    f.nome                        AS fornecedor_nome,
    cl_forn.nome                  AS cidade_fornecedor_nome,
    cl_forn.estado                AS cidade_fornecedor_estado

FROM vendas v

JOIN lojas l                ON v.id_loja = l.id_loja
JOIN cidades cl_loja        ON l.id_cidade = cl_loja.id_cidade

JOIN vendedores vend        ON v.id_vendedor = vend.id_vendedor

JOIN clientes c             ON v.id_cliente = c.id_cliente
JOIN cidades cl_cli         ON c.id_cidade = cl_cli.id_cidade

JOIN itens_venda iv         ON v.id_venda = iv.id_venda

JOIN produtos p             ON iv.id_produto = p.id_produto
JOIN categorias cat         ON p.id_categoria = cat.id_categoria
JOIN fornecedores f         ON p.id_fornecedor = f.id_fornecedor
JOIN cidades cl_forn        ON f.id_cidade = cl_forn.id_cidade
;


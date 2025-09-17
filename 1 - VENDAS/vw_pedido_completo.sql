CREATE view Pedido_completo as

select v.id_venda, c.id_cliente, p.nome_produto, ct.nome_categoria, v.quantidade ,p.valor_unitario * v.quantidade as valor_total, v.data_venda from vendas v
inner join produtos p
on v.id_produto = p.id_produto
inner join clientes c
on c.id_cliente = v.id_cliente
inner join categorias ct
on p.id_categoria = ct.id_categoria
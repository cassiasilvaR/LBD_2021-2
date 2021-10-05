select f.nome, 
       coalesce(count(p.id_fornecedor), 0) qtd_produtos,
       coalesce(sum(p.qtd_estoque), 0) qtd_estoque
    from fornecedor f
        left join produto p on p.id_fornecedor = f.id
    group by f.nome
    order by f.nome desc;
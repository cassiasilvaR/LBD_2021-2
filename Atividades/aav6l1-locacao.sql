select c.id,
       c.nome
    from cliente c
    where c.id not in (select id_cliente from locacao)
       
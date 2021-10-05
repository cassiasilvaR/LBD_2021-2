select distinct f.titulo
    from filme f
        inner join avaliacao c on c.idt_filme = f.idt_filme 
    where c.classificacao in (3, 5) and
          f.titulo like '_o%'       and 
          f.titulo like '%1995%'
    order by f.titulo

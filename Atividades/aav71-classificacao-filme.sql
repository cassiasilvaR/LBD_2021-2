select f.titulo, 
       g.nome
    from filme f
        inner join filme_genero fg on f.idt_filme  = fg.idt_filme
        inner join genero       g  on g.idt_genero = fg.idt_genero 
    where g.nome like '%Action%' or
          g.nome like '%Horro%'  or 
          g.nome like '%Wars%'
    order by f.titulo desc;
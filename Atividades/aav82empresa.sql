select f.pnome,
       f.cpf,
       f.salario
    
    from funcionario f
    
    where f.cpf not in (select fcpf from trabalha_em)
    order by 3 asc 
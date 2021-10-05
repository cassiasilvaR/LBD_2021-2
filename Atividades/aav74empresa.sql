select f.* 
    from funcionario f 
    where f.cpf not in (select fcpf from dependente)
    order by 1 desc
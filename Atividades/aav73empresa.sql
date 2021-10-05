select f.pnome,
       f.cpf,
       f.salario,
       d.dnome
    from funcionario f
        inner join departamento d on d.dnumero = f.dnr
    where f.cpf in (select cpf_supervisor from funcionario)
    order by f.pnome
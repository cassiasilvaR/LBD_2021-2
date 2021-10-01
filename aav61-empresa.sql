select pnome,
       salario

    from funcionario f
        inner join departamento d on d.dnumero = f.dnr
    
    where f.salario > (select avg(salario) 
                            from funcionario a 
                                inner join departamento b on b.dnumero = a.dnr 
                            where d.dnumero = b.dnumero)
    
    order by d.dnumero;
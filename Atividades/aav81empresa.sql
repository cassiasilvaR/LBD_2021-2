select f.cpf

from funcionario f 
    inner join funcionario  s on s.cpf         = f.cpf_supervisor
    inner join departamento d on d.cpf_gerente = f.cpf
order by 1 asc
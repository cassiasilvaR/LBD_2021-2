select distinct al.des_nome
    
    from
        (select distinct idt_aluno2 idt_aluno
            from amigo 
            where idt_aluno1 in (1689, 1381)) am
    
        inner join aluno al on al.idt_aluno = am.idt_aluno
    
    where al.idt_aluno in (select distinct idt_aluno2 
                                from amigo am
                                    
                                where am.idt_aluno1 = 1381)
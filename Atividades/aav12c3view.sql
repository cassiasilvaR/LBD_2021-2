--select * from vpartida_classificacao
--create view vpartida_classificacao as                 A SAÍDA ESPERADA ESTÁ COM ERRO, NÃO ESTÁ ORDENADO PELO ID!
    select  id, 
            nome_time_1,
            nome_time_2,
            case 
                when time_1_gols > time_2_gols
                    then nome_time_1
                when time_1_gols = time_2_gols  
                    then 'EMPATE'
                else nome_time_2
            end classificacao_vencedor
        from vpartida
        order by id asc;
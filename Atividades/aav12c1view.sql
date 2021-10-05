create view vpartida AS 
    select p.id, 
           time_1, 
           time_2, 
           time_1_gols, 
           time_2_gols,
           case 
            when time_1 = t.id 
                then nome 
           end nome1, 
           (select nome from time where id = p.time_2) nome2
        from partida p
            inner join time t on t.id = time_1 
        order by p.id asc;
-- COR = 1
-- SP  = 2
-- CRU = 3
-- ATM = 4
-- PAL = 5
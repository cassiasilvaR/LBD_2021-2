select a_max.nome,
       max(a_max.numero_cliente)
    
    from advogado a_max 

union 

select a_min.nome,
       min(a_min.numero_cliente)

    from advogado a_min
    
union 

select 'Média' nome,
       round(avg(a_med.numero_cliente), 0)

    from advogado a_med

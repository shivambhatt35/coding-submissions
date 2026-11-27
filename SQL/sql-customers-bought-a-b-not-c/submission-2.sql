with base as(

    select 
        c.customer_id,
        c.customer_name,
        sum(case when o.product_name = 'A' then 1 else 0 end) as sum_a,
        sum(case when o.product_name = 'B' then 1 else 0 end) as sum_b,
        sum(case when o.product_name = 'C' then 1 else 0 end) as sum_c
    from orders o
    left join customers c
    on o.customer_id = c.customer_id
    group by 1,2
)

select  customer_id,
        customer_name
from base
where sum_a >= 1 and sum_b >= 1 and sum_c = 0
order by customer_name
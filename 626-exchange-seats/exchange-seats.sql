with base as(

select 
    id, 
    lead(id) over (order by id) as lead_id,
    lag(id) over (order by id) as lag_id,
    student
from seat
),

base2 as (
select 
    id, lead_id, lag_id,
    case 
        when id % 2 = 0 then lag_id 
        else lead_id
    end as flag,
    student
from base
)

select COALESCE(flag,id) as id, student
from base2
order by 1
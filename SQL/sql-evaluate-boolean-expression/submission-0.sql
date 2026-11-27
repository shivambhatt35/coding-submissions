with base as (

    select
        e.left_operand,
        v.value as value_one,
        e.operator,
        w.value as value_two,
        e.right_operand
    from expressions e
    left join variables v
    on v.name = e.left_operand
    left join variables w
    on w.name = e.right_operand
)

select 
    left_operand,
    operator,
    right_operand,
        case 
        when operator = '>' and value_one > value_two then 'true' 
        when operator = '<' and value_one < value_two then 'true' 
        when operator = '=' and value_one = value_two then 'true' 
        else 'false'
    end as value

from base
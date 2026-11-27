-- Write your query below
with base as(
select 
    student_id,
    exam_id,
    score,
    rank() over (partition by student_id order by score desc, exam_id asc) as rank_
from exam_results
)

select 
    student_id,
    exam_id,
    score
from base where rank_ = 1
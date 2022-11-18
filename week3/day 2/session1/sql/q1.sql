select
    department_name,
    count(1) as n
from
    employee
    join department using (department_id)
group by
    department_name
order by
    2 desc;
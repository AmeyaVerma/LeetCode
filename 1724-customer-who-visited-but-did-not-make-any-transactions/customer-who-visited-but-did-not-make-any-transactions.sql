select v.customer_id,COUNT(v.visit_id) AS count_no_trans  
from visits v
left join transactions t
on v.visit_id=t.visit_id
where t.visit_id is null
group by v.customer_id;
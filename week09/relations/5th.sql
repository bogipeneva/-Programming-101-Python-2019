select name
from movieexec
where networth > (select networth from movieexec where name like 'Merv Griffin');
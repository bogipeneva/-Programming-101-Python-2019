select title
from movie
where length > (select length from movie where title like 'Gone With the Wind');

select * from movie;



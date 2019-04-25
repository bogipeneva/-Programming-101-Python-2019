select name
from moviestar
where name in (select starname
from starsin 
where movietitle ='Terms of Endearment') and gender like 'M';
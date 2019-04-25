select starname
from starsin
where movietitle in (select title
from movie 
where studioname like 'MGM') and movieyear = 1995;
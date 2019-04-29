
select AVG(speed)
from pc

SELECT product.maker,AVG(laptop.screen) AS avgScreen FROM Laptop
LEFT JOIN Product ON product.model = laptop.model
GROUP BY product.maker;

select AVG(speed)
from pc
where price > 1000;

SELECT hd,AVG(price) AS avgPrice 
FROM pc
GROUP BY hd;


SELECT speed,AVG(price) AS avgPrice 
FROM pc
where speed > 500
GROUP BY pc.speed;

select AVG(price)
from pc
where model in (select model from product where maker = 'A');

select AVG(price)
from pc
where model in (select model from Product where maker = 'A');

select maker, COUNT(model)
from product
where type = 'PC'
GROUP BY maker;

select maker, COUNT(*) as num
from product
where type = 'PC'
group by maker
having num > 2;

select maker, MAX(price)
from product
LEFT join pc on product.model == pc.model;

select AVG(ram)
from product
left join pc on product.model == pc.model
where type == 'PC' and maker in (select  maker from product where type == 'Printer');


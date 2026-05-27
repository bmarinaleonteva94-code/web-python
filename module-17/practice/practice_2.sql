create database Birds;

alter database Birds rename to Cats;

drop database Cats;

CREATE TABLE fruits_and_vegetables(
	id int PRIMARY KEY,
    name text NOT NULL,
    type text NOT null check (type IN ('овощ', 'фрукт')),
    color text,
    calories int,
    description text
);

INSERT INTO fruits_and_vegetables (name, type, color, calories, description)
values
    ('Огурец', 'овощ', 'зеленый', 20, 'зеленый овощ'),
    ('Яблоко', 'фрукт', 'красный', 60, 'круглое'),
    ('Помидор', 'овощ', 'красный', 50, 'круглое');

select * from fruits_and_vegetables;

select * from fruits_and_vegetables where type = 'овощ';

select * from fruits_and_vegetables where type = 'фрукт';

select name from fruits_and_vegetables;

select distinct color from fruits_and_vegetables;

select * from fruits_and_vegetables 
where type = 'фрукт' and color = 'красный';

select * from fruits_and_vegetables 
where type = 'овощ' and color = 'зеленый';


--------------------------------------------------------------------------

select * from fruits_and_vegetables
where type = 'овощ' and calories < 50;

select * from fruits_and_vegetables 
where type = 'фрукт' and calories between 20 and 50;

select * from  fruits_and_vegetables  where name like '%капуста%';

select * from fruits_and_vegetables 
where description like '%круг%';

select * from fruits_and_vegetables
where color in ('красный', 'желтый');


---------------------------------------------------------------------------

select count (*) as vegetable_count
from fruits_and_vegetables
where type = 'овощ'

select count (*) as fruit_count
from fruits_and_vegetables
where type = 'фрукт'

select count(*) as count_by_color
from fruits_and_vegetables
where color = 'красный';

select color, count(*) as count
from fruits_and_vegetables
group by color;

select color, count(*) as min_count
from fruits_and_vegetables
group by color 
order by min_count asc
limit 1;

select color, count(*) as max_count
from fruits_and_vegetables
group by color 
order by max_count desc
limit 1;

select min(calories) as min_calories
from fruits_and_vegetables;

select max(calories) as max_calories
from fruits_and_vegetables;

select round(avg(calories), 2) as avg_calories
from fruits_and_vegetables;

select name, calories
from fruits_and_vegetables
where type = 'фрукт'
order by calories asc
limit 1;

select name, calories 
from fruits_and_vegetables
where type = 'фрукт'
order by calories desc 
limit 1;
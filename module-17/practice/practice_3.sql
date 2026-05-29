create table departments (
	id serial primary key,
	financing numeric(15,2) not null default 0 check (financing>=0),
	name varchar(255) not null unique
);

create table faculties (
	id serial primary key,
	dean varchar(255) not null,
	name varchar(255) not null unique 
);

create table groups (
	id serial primary key,
	name varchar(255) not null unique,
	rating numeric(2,1) not null check (rating>=0 and rating<=5),
	year integer not null check (year>=1 and year<=5)
);

create table teachers (
	id serial primary key,
	EmploymentDate date not null check (EmploymentDate>='1990-01-01'),
	IsAssistant boolean not null default false,
	IsProfessor boolean not null default false,
	name varchar(255) not null,
	position varchar(255) not null,
	premium numeric(10,2) not null default 0 check (premium>=0),
	salary numeric(10,2) not null check (salary>0),
	surname varchar(255) not null 
);

------------------------------------------------------------------------

insert into departments (financing, name)
values 
	(150000, 'Кафедра математики'),
	(200000, 'Кафедра физики'),
	(180000, 'Кафедра биологии'),
	(220000, 'Кафедра информатики'),
	(190000, 'Кафедра химии');

insert into faculties (dean, name)
values 
	('Иванов И. Т.', 'Физико-математический факультет'),
	('Козлов К. К.', 'Факультет информационных технологий'),
	('Петров П. Р.', 'Химико-биологический факультет'),
	('Круглов Д. Н.', 'Гуманитарный факультет'),
	('Семенов С. С.', 'Естественно-научный факультет');

insert into groups (name, rating, year)
values 
	('М‑101', 4.5, 1),
	('Ф‑201', 3.8, 2),
	('И‑301', 4.2, 3),
	('Х‑401', 3.9, 4),
	('Б‑501', 4.1, 5),
	('М‑102', 4.0, 1),
	('И‑302', 4.7, 3);

insert into teachers (EmploymentDate, IsAssistant, IsProfessor, name, position, premium, salary, surname) 
values 
	('1995-03-15', false, true , 'Александр', 'Профессор', 15000.00, 85000.00, 'Смирнов'),
	('2001-09-01', true, false, 'Мария', 'Ассистент', 5000.00, 45000.00, 'Иванова'),
	('1998-02-20', false, false, 'Дмитрий', 'Доцент', 10000.00, 65000.00, 'Кузнецов'),
	('2010-08-25', true, false, 'Елена', 'Старший преподаватель', 7000.00, 55000.00, 'Попова'),
	('2005-06-12', false, true, 'Сергей', 'Профессор', 20000.00, 90000.00, 'Волков'),
	('2015-09-01', false, false, 'Анна', 'Преподаватель', 3000.00, 40000.00, 'Морозова'),
	('2012-03-18', true, false, 'Игорь', 'Ассистент', 4000.00, 42000.00, 'Лебедев');

----------------------------------------------------------------------------------

select name, financing, id
from departments;

select 
	groups.name as "Название группы",
	groups.rating as "Рейтинг группы"
from groups;

select 
	name,
	(premium * 100.0 / salary) as "Процент надбавки от ставки",
	(salary * 100.0 / (salary + premium)) as "Процент ставки от общей суммы"
from teachers;

select 
	'The dean of faculty ' || name || ' is ' || dean || '.' as FacultyInfo
from faculties;

select surname
from teachers 
where IsProfessor = true and salary > 70000;

select name 
from departments
where financing < 170000 or financing > 200000;

select name
from faculties 
where name != 'Химико-биологический факультет';

select surname, position 
from teachers 
where IsProfessor = true;

select surname, position, salary, premium
from teachers 
where IsAssistant = true and premium between 4500 and 6000;

select surname, salary
from teachers 
where IsAssistant = true;

select surname, position, EmploymentDate
from teachers
where EmploymentDate < '2000-01-01'
order by EmploymentDate asc;

select 
	name as "Name of Department"
from departments 
order by name asc;

select surname
from teachers
where IsAssistant = true and (salary + premium) <= 50000;

select name 
from groups 
where year = 5 and rating between 2 and 4;

select surname 
from teachers 
where IsAssistant = true and (salary < 45000 or premium < 6000);
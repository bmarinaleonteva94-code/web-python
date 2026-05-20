create table departments (
	id serial primary key,
	name text not null unique
);

create table employees (
	id serial primary key,
	name text not null,
	salary numeric (10,2) check (salary > 0),
	department_id int references departments(id),
	hired_at date default current_date
);

create table projects(
	id serial primary key,
	name text not null,
	employee_id int references employees(id),
	budget numeric(12, 2) check (budget >= 0),
	is_active boolean default true
);

-- -------------------------------------------

insert into departments (name)
values 
	('IT'),
	('HR'),
	('Finance'),
	('Marketing');

insert into employees (name, salary, department_id, hired_at)
values 
	('Анна Иванова', 150000, 1, '2023-01-15'),
	('Иван Петров', 90000, 1, '2023-03-10'),
	('Мария Смирнова', 110000, 2, '2022-11-20'),
	('Олег Кузнецов', 130000, 3, '2021-06-05'),
	('Алексей Орлов', 70000, null, '2024-02-01'),
	('Елена Соколова', 160000, 1, '2020-09-12');

insert into projects (name, employee_id, budget, is_active)
values 
	('CRM System', 1, 500000, TRUE),
	('Website Redesign', 2, 200000, TRUE),
	('Hiring Platform', 3, 300000, TRUE),
	('Accounting Automation', 4, 350000, FALSE),
	('Internal Chat', 1, 150000, TRUE);


select name, 
	salary,
	case 
		when salary >= 150000 then 'high'
		when salary >= 100000 then 'middle'
		else 'low'
	end as salary_level
from employees;
	
select e.name as employee_name, coalesce(d.name, 'без отдела') as department_name
from employees e 
left join departments d on e.department_id = d.id; 

select 
	d.id,
	d.name
from departments d
where exists (
	select 1 from employees e
	where e.department_id  = d.id 
);

select 
	e.id,
	e.name
from departments e
where exists (
	select 1 from projects p
	where p.employee_id = e.id 
)

select name as project_name,
	budget,
	case 
		when is_active = true then 'active'
		else 'close'
	end as project_status
from projects;
	
select 
	e.name as employee_name,
	count(p.id) as projects_count
from employees e 
left join projects p on p.employee_id = e.id
group by e.id, e.name
order by projects_count desc;

UPDATE projects
SET budget = budget + 50000
WHERE is_active = true
returning id, name, employee_id, budget, is_active;

DELETE FROM projects 
WHERE is_active = false
returning id, name;

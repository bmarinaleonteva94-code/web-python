create table faculties (
	id serial primary key,
	dean varchar(255) not null,
	name varchar(255) not null unique 
);

create table departments (
	id serial primary key,
	financing numeric(15,2) not null default 0 check (financing>=0),
	name varchar(255) not null unique,
	faculty_id integer not null,
	FOREIGN KEY (faculty_id) references faculties (id) 
);

create table groups (
	id serial primary key,
	name varchar(255) not null unique,
	rating numeric(2,1) not null check (rating>=0 and rating<=5),
	year integer not null check (year>=1 and year<=5),
	faculty_id integer not null,
	foreign key (faculty_id) references faculties(id)
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
	surname varchar(255) not null,
	department_id integer not null,
	foreign key (department_id) references departments(id)
);

------------------------------------------------------------------------

insert into faculties (dean, name)
values 
	('Ильин И. Т.', 'Физико-математический факультет'),
	('Соколов К. К.', 'Химико-биологический факультет'),
	('Орлов П. Р.', 'Факультет информационных технологий'),
	('Кольцов Д. Н.', 'Исторический факультет'),
	('Сорокин С. С.', 'Факультет иностранных языков');

insert into departments (financing, name, faculty_id)
values 
	(500000.00, 'Кафедра математики', 1),
	(1000000.00, 'Кафедра биологии', 2),
	(900000.00, 'Кафедра физики', 1),
	(700000.00, 'Кафедра информатики', 3),
	(1100000.00, 'Кафедра химии', 2),
	(950000.00, 'Кафедра истории', 4),
	(750000.00, 'Кафедра английского языка', 5);

insert into groups (name, rating, year, faculty_id) 
values 
	('A-101', 4, 1, 1),
	('B-200', 3, 3, 2),
	('C-300', 5, 4, 3),
	('A-103', 4.8, 5, 1),
	('B-204', 3.7, 2, 2),
	('C-309', 4.4, 3, 3),
	('A-105', 3.2, 5, 1);

insert into teachers (EmploymentDate, IsAssistant, IsProfessor, name, position, premium, salary, surname, department_id) 
values 
	('2000-09-01', true, false , 'Иван', 'Ассистент', 5000.00, 50000.00, 'Иванов', 1),
	('2002-07-30', false, true, 'Петр', 'Преподаватель', 20000.00, 70000.00, 'Петров', 3),
	('2009-01-04', false, true, 'Ольга', 'Доцент', 20000.00, 90000.00, 'Сидорова', 4),
	('2015-05-06', true, false, 'Василий', 'Ассистент', 10000.00, 40000.00, 'Кошкин', 1),
	('1992-12-23', false, true, 'Артем', 'Профессор', 15000.00, 100000.00, 'Круглов', 2),
	('2007-03-30', false, true, 'Сергей', 'Преподаватель', 20000.00, 75000.00, 'Козлов', 5),
	('2009-08-14', false, true, 'Семен', 'Преподаватель', 15000.00, 95000.00, 'Семенов', 6);

----------------------------------------------------------------------------------

select name, financing, id
from departments;

select 
	groups.name as "Название группы",
	groups.rating as "Рейтинг группы"
from groups;

select 
	name,
	ROUND((premium * 100.0 / salary), 2) as "Процент надбавки от ставки",
	ROUND((salary * 100.0 / (salary + premium)), 2) as "Процент ставки от общей суммы"
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

-----------------------------------------------------------------------------

create table curators (
	id serial primary key,
	name varchar(255) not null check (name != ''),
	surname varchar(255) not null check (surname!='')
);

insert into curators (name, surname)
values 
	('Анна', 'Иванова'),
	('Петр', 'Петров'),
	('Иван', 'Иванов'),
	('Алексей', 'Кошкин'),
	('Сергей', 'Сергеев');

ALTER TABLE groups
ADD COLUMN CuratorId integer; 

UPDATE groups
SET CuratorId = CASE
    WHEN name = 'A-101' THEN 1     
    WHEN name = 'B-200' THEN 2 
	WHEN name = 'C-300' THEN 3 
    WHEN name = 'A-103' THEN 4 
    WHEN name = 'B-204' THEN 5 
    WHEN name = 'C-309' THEN 1 
    WHEN name = 'A-105' THEN 3 
END;

SELECT * FROM groups WHERE CuratorId IS NULL;

ALTER TABLE groups ALTER COLUMN CuratorId SET NOT NULL;

ALTER TABLE groups
ADD CONSTRAINT fk_groups_curator
FOREIGN KEY (CuratorId)
REFERENCES curators(id)
ON DELETE SET NULL;

--------------------------------------------------------------------

alter table faculties 
add column financing numeric(15,2) default 0 not null;

UPDATE faculties
SET financing = CASE
    WHEN name = 'Физико-математический факультет' THEN 1500000
    WHEN name = 'Факультет информационных технологий' THEN 2000000
    WHEN name = 'Химико-биологический факультет' THEN 1800000
    WHEN name = 'Исторический факультет' THEN 1200000
    WHEN name = 'Факультет иностранных языков' THEN 1600000
	ELSE 0
END;

ALTER TABLE faculties
ADD CONSTRAINT check_faculties_financing_positive
CHECK (Financing >= 0);

----------------------------------------------------------

ALTER TABLE groups ADD COLUMN DepartmentId integer;

UPDATE groups
SET DepartmentId = CASE
    WHEN name = 'A-101' THEN 1 
    WHEN name = 'B-200' THEN 5
    WHEN name = 'C-300' THEN 4  
    WHEN name = 'A-103' THEN 1 
    WHEN name = 'B-204' THEN 5 
    WHEN name = 'C-309' THEN 4 
    WHEN name = 'A-105' THEN 1 
END;

ALTER TABLE groups ALTER COLUMN DepartmentId SET NOT NULL;

ALTER TABLE groups
ADD CONSTRAINT fk_groups_departments
FOREIGN KEY (DepartmentId) REFERENCES departments(Id);

----------------------------------------------------------------------------

create table subjects(
	id serial primary key,
	name varchar(255) not null unique check (name != '')
);

insert into subjects (name)
values 
	('Математика'),
	('Физика'),
	('Информатика'),
	('Химия'),
	('Биология'),
	('История'),
	('Английский язык');

----------------------------------------------------------------------------

create table lectures (
	id serial primary key,
	LectureRoom varchar(255) not null check (LectureRoom != ''),
	SubjectId integer not null ,
	TeacherId integer not null,
	foreign key (SubjectId) references subjects(id) on delete restrict,
	foreign key (TeacherId) references teachers(id) on delete cascade
);

insert into lectures (LectureRoom, SubjectId, TeacherId)
values 
	('A-101', 1,1),
	('B-202', 2,2),
	('C-300', 3,3),
	('M-110', 4,4),
	('A-103', 5,5),
	('D-500', 6,6),
	('B-100', 7,7);

-----------------------------------------------------------------------------

create table GroupsCurators(
	id serial primary key,
	curatorId integer not null,
	groupId integer not null,
	foreign key (CuratorId) references curators(id),
	foreign key (GroupId) references groups(id)
);

insert into GroupsCurators (curatorId, groupId)
values 
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(1,6),
	(5,5),
	(4,7);

----------------------------------------------------------

create table GroupsLectures(
	id serial primary key,
	GroupId integer not null,
	LectureId integer not null,
	foreign key (GroupId) references groups(id),
	foreign key (LectureId) references lectures(id) 
);

insert into GroupsLectures (GroupId, LectureId)
values 
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5), 
	(6,1),
	(7,3);

----------------------------------------------------------------------

SELECT t.name AS "Имя преподавателя",
       t.surname AS "Фамилия преподавателя",
       g.name AS "Название группы"
FROM teachers t
CROSS JOIN groups g
ORDER BY t.surname, t.name, g.name;

SELECT DISTINCT f.name AS "Название факультета"
FROM faculties f
JOIN departments d ON f.id = d.facultyId
WHERE d.financing > f.financing;

SELECT c.surname AS "Фамилия куратора",
       g.name AS "Название группы"
FROM GroupsCurators gc
JOIN curators c ON gc.CuratorId = c.id
JOIN groups g ON gc.GroupId = g.id
ORDER BY c.surname, g.name;

SELECT DISTINCT t.name AS "Имя преподавателя",
       t.surname AS "Фамилия преподавателя"
FROM lectures l
JOIN GroupsLectures gl ON l.id = gl.LectureId
JOIN groups g ON gl.GroupId = g.id
JOIN teachers t ON l.TeacherId = t.id
WHERE g.name = 'A-101'
ORDER BY t.surname , t.name;

SELECT
    t.surname AS "Фамилия преподавателя",
    f.name AS "Название факультета"
FROM teachers t
JOIN departments d ON t.DepartmentId = d.id
JOIN faculties f ON d.FacultyId = f.id
ORDER BY f.name, t.surname;

SELECT DISTINCT
    d.name AS "Название кафедры",
    g.name AS "Название группы"
FROM groups g
JOIN faculties f ON g.FacultyId = f.id
JOIN departments d ON f.id = d.FacultyId
ORDER BY d.name, g.name;

SELECT DISTINCT
    s.name AS "Название дисциплины"
FROM subjects s
JOIN lectures l ON s.id = l.SubjectId
JOIN teachers t ON l.TeacherId = t.id
WHERE t.name = 'Петр' AND t.surname = 'Петров'
ORDER BY s.name;

SELECT DISTINCT
    d.name AS "Название кафедры"
FROM departments d
JOIN teachers t ON d.id = t.DepartmentId
JOIN lectures l ON t.id = l.TeacherId
JOIN subjects s ON l.SubjectId = s.id
WHERE s.name = 'Математика'
ORDER BY d.name;

SELECT
    g.name AS "Название группы"
FROM groups g
JOIN faculties f ON g.FacultyId = f.id
WHERE f.name = 'Физико-математический факультет'
ORDER BY g.name;

SELECT
    g.name AS "Название группы",
    f.name AS "Название факультета"
FROM groups g
JOIN faculties f ON g.FacultyId = f.id
WHERE g.year = 5
ORDER BY f.name, g.name;

SELECT
    t.name AS "Имя преподавателя",
    t.surname AS "Фамилия преподавателя",
    s.name AS "Название дисциплины",
    g.name AS "Название группы",
    l.LectureRoom AS "Аудитория"
FROM teachers t
JOIN lectures l ON t.id = l.TeacherId
JOIN subjects s ON l.SubjectId = s.id
JOIN GroupsLectures gl ON l.id = gl.LectureId
JOIN groups g ON gl.GroupId = g.id
WHERE l.LectureRoom = 'A-101'
ORDER BY t.surname, t.name, s.name;

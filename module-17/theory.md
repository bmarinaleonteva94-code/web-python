# база данных 
### `CREATE`  
создает таблицу, базу, индекс
```sql
CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    salary NUMERIC
)
```
### `TABLE` 
Указывает, что создается или изменяется таблица
```sql
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name TEXT
);
```
### `ALTER`
ИЗМЕНЯЕТ СУЩЕСТВУЮЩИЙ ОБЪЕКТ
```sql
ALTER TABLE employees 
ADD COLUMN email TEXT;
```
### `ADD`
добавляет колонку, ограничения
```sql
ALTER TABLE employees 
ADD COLUMN phone TEXT;
```
### `DROP`
УДАЛЯЕТ ОБЪЕКТ (ТАБЛИЦУ)
```sql
DROP TABLE projects;
```
### `IF EXISTS`
ПОЗВОЛЯЕТ ИЗБЕЖАТЬ ОШИБКИ, ЕСЛИ ОБЪЕКТА НЕТ
```sql
DROP TABLE IF EXISTS old_projects;
```
### `IF NOT EXISTS`
СОЗДАЕТ ОБЪЕКТ, ТОЛЬКО ЕСЛИ ОН ЕЩЕ НЕ СУЩЕСТВУЕТ
```sql
CREATE TABLE IF NOT EXISTS departments(
  id SERIAL PRIMARY KEY,
  name TEXT
);
```
### `RENAME`
ПЕРЕИМЕНОВЫВАЕТ ОБЪЕКТ
```sql
ALTER TABLE employees
RENAME COLUMN name to full_name;
```
### `TRUNCATE`
БЫСТРО ОЧИЩАЕТ ТАБЛИЦУ
```sql
TRUNCATE TABLE projects;
```
## 2. Работа с данными
### `SELECT`
выбирает данные
```sql
SELECT name, salary FROM employees;
```
### `FROM`
Указывает источник данных
```sql
SELECT name, salary FROM employees;
```
### `INSERT`
Добавляет строки
```sql
INSERT INTO departments(name)
VALUES (`it`), (`HR`), (`Finance`);
```
### `INTO`
УКАЗЫВАЕТ, КУДА ВСТАВЛЯТЬ ДАННЫЕ
```sql
INSERT INTO employees(name, salary, department_id)
VALUES (`Анна`, 1200, 1);
```
### `VALUES`
ПЕРЕДАЕТ КОНКРЕТНЫЕ ЗНАЧЕНИЯ
```sql
INSERT INTO projects(name, employee_id, budget)
VALUES (`CRM System`, 1, 55555);
```

### `UPDATE`
обновляет строки
```sql
UPDATE employees
SET salary = salary * 1.10
WHERE department_id = 1;
```

### `SET`
задает новые значения при использовании UPDATE
```sql
UPDATE projects
SET is_active = FALSE,
    is_active2 = FALSE
WHERE budget < 10000;
```

### `DELETE`
УДАЛЯЕТ СТРОКИ 
```SQL
DELETE FROM employees 
WHERE salary < 50000;
```

##  3. Фильтрация данных

### `WHERE`
ФИЛЬТРУЕТ СТРОКИ
```sql
SELECT *
FROM employees 
WHERE salary > 100000;
```

### `AND`
ОБА УСЛОВИЯ ДОЛЖНЫ БЫТЬ ИСТИННЫМИ
```sql
SELECT *
FROM employees 
WHERE salary > 100000
    AND department_id = 1;
```

### `OR`
Одно из усдовий должно БЫТЬ ИСТИННЫМ
```sql
SELECT *
FROM employees 
WHERE salary > 100000
    OR department_id = 1;
```

### `NOT`
ОТРИЦАНИЕ УСЛОВИЯ
```sql
SELECT *
FROM projects 
WHERE NOT is_active
```

### `IN`
ПРОВЕРЯЕТ, ВХОДИТ ЛИ ЗНАЧЕНИЕ В СПИСОК
```sql
SELECT * 
FROM employees
WHERE department_id IN (1,2);
```

### `NOT IN`
ПРОВЕРЯЕТ, ЧТО ЗНАЧЕНИЯ НЕТ В СПИСКЕ
```sql
SELECT *
FROM employees
WHERE department_id NOT IN (1,2);
```

### `BETWEEN`
ПРОВЕРЯЕТ ДИАПАЗОН
```sql
SELECT *
FROM employees
WHERE salary BETWEEN 80000 AND 150000;
```

### `LIKE`
ПОИСК ПО ШАБЛОНУ
```sql
SELECT *
FROM employees
WHERE name LIKE "A%";
```

### `ILIKE`
ПОИСК ПО ШАБЛОНУ БЕЗ УЧЕТА РЕГИСТРА
```sql
SELECT *
FROM employees
WHERE name ILIKE "A%";
```

### `IS NULL`
ПРОВЕРЯЕТ ЗНАЧЕНИЕ НА "NULL"
```sql
SELECT *
FROM employees
WHERE department_id IS NULL;
```

### `IS NOT NULL`
ПРОВЕРЯЕТ, ЧТО ЗНАЧЕНИЕ НЕ NULL
```sql
SELECT *
FROM employees
WHERE department_id IS NOT NULL;
```

### `EXISTS`
Проверяет, существуют ли строки 
```sql
SELECT *
FROM departments AS d
WHERE EXISTS (
    SELECT 1
    FROM employees AS e
    WHERE e.departments_id = d.id
)
```


## 4. Сортировка и ограничение результата

### `ORDER BY`
Сортирует результат
```sql
SELECT *
FROM employees
ORDER BY salary;
```

### `ASC`
Сортирует по возрастанию
```sql
SELECT *
FROM employees
ORDER BY salary ASC;
```

### `DESC`
Сортирует результат по убыванию
```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

### `LIMIT`
Ограничивает количество строк
```sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;
```

### `OFFSET`
ПРОПУСКАЕТ УКАЗАННОЕ КОЛИЧЕСТВО СТРОК
```sql
SELECT *
FROM employees
ORDER BY id
LIMIT 10 OFFSET 20;
```

## 5. Группировка и агрегаты

### `GROUP BY`
Группирует строки
```sql
SELECT department_id, COUNT(*) as employee_count
FROM employees
GROUP BY department_id;
```

### `HAVING`
Фильтрует данные после группировки
```sql
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 100000;
```

### `COUNT`
Считает количество строк
```sql
SELECT COUNT(*)
FROM employees;
```

### `SUM`
Суммирует значение
```sql
SELECT SUM(budget)
FROM projects;
```

### `AVG`
Считает среднее значение
```sql
SELECT AVG(salary)
FROM employees;
```

### `MIN`
минимальное значение
```sql
SELECT MIN(salary)
FROM employees;
```

### `MAX`
максимальное значение
```sql
SELECT MAX(salary)
FROM employees;
```

### `DISTINCT`
УБИРАЕТ ДУБЛИКАТЫ
```sql
SELECT DISTINCT department_id
FROM employees;
```


## 6. Соединение таблиц

### `JOIN`
СОЕДИНЯЕТ ТАБЛИЦЫ
```sql
SELECT e.name, d.name AS department
FROM employees AS e
JOIN departments d ON e.department_id = d.id;
```

### `INNER JOIN`
ПОКАЗЫВАЕТ ТОЛЬКО СОВПАВШИЕ СТРОКИ
```sql
SELECT e.name, P.name AS project
FROM employees AS e
INNER JOIN projects p ON p.employee_id = e.id;
```

### `LEFT JOIN`
СОЕДИНЯЕТ ТАБЛИЦЫ, ПОКАЗЫВАЕТ ВСЕ СТРОКИ ИЗ ЛЕВОЙ ТАБЛИЦЫ, ДАЖЕ ЕСЛИ СПРАВА НЕТ СОВПАДЕНИЙ
```sql
SELECT e.name, p.name AS project
FROM employees AS e
LEFT JOIN projects p ON p.employee_id = e.id;
```

### `RIGHT JOIN`
СОЕДИНЯЕТ ТАБЛИЦЫ, ПОКАЗЫВАЕТ ВСЕ СТРОКИ ИЗ ПРАВОЙ ТАБЛИЦЫ, ДАЖЕ ЕСЛИ СЛЕВА НЕТ СОВПАДЕНИЙ
```sql
SELECT e.name, p.name AS project
FROM employees AS e
RIGHT JOIN projects p ON p.employee_id = e.id;
```

### `FULL JOIN`
ПОКАЗЫВАЕТ ВСЕ СТРОКИ ИЗ ОБЕИХ ТАБЛИЦ
```sql
SELECT e.name, p.name AS project
FROM employees AS e
FULL JOIN projects p ON p.employee_id = e.id;
```

### `ON`
УСЛОВИЕ СОЕДИНЕНИЯ
```sql
SELECT *
FROM employees AS e
JOIN departments d ON e.department_id = d.id;
```


## 7. Алиасы
### `AS`
Дает псевдоним колонке или таблице
```sql
SELECT name AS employee_name,
    salary AS monthly_salary
FROM employees AS e;
```

```sql
SELECT e.name
FROM employees e;
```


## 8. Ограничение таблиц

### `PRIMARY KEY`
главный ключ 
```sql
CREATE TABLE departments(
    id SERIAL PRIMARY KEY,
    name TEXT
)
```

### `FOREIGN KEY`
ВНЕШНИЙ ключ 
```sql
CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    name TEXT,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments (id)
)
```

короткая запись
```sql
department_id INT REFERENCES departments(id)
```

### `REFERENCES`
указывает, на какую таблицу и колонку ссылается ключ
```sql
department_id INT REFERENCES departments(id)
```

### `NOT NULL`
ЗАПРЕЩАЕТ NULL
```sql
name TEXT NOT NULL
```

### `NULL`
ОТСУТСТВУЕТ ЗНАЧЕНИЕ
```sql
INSERT INTO employees (name, salary, department_id)
VALUES ('Иван', NULL, 1);
```

### `UNIQUE`
ЗНАЧЕНИЕ ДОЛЖНО БЫТЬ УНИКАЛЬНЫМ
```sql
ALTER TABLE employees
ADD CONSTRAINT unique_employee_email UNIQUE (email);
```

### `CONSTRAINT`
ДАЕТ ИМЯ ОГРАНИЧЕНИЮ
```sql
ALTER TABLE employees
ADD CONSTRAINT salary_positive CHECK(salary > 0);
```

### `CHECK`
ПРОВЕРЯЕТ УСЛОВИЕ
```sql
ALTER TABLE employees
ADD CONSTRAINT salary_positive CHECK (salary > 0);
```

### `DEFAULT`
ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ
```sql
ALTER TABLE projects
ALTER COLUMN is_active SET DEFAULT TRUE;
```

## 9. Типы данных

### `INT/INTEGER`
для хранения целых чисел
```sql
CREATE TABLE employees(
    id INT,
    name TEXT,
    age INT
)
```

### `SMALLINT`
для хранения целых чисел от -32000 до 32000
```sql
CREATE TABLE products(
    id INT,
    name TEXT,
    rating SMALLINT
)
```

### `BIGINT`
для хранения больших целых чисел 
```sql
CREATE TABLE videos(
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL,
    views BIGINT DEFAULT 0
)
```

### `SERIAL`
создает автоматически увеличивающийся числовой id, устарело
```sql
CREATE TABLE departments(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
)
```

### `GENERATED`
ГЕНЕРИРУЕТ ЗНАЧЕНИЕ СРЕДСТВАМИ БАЗЫ ДАННЫХ
```sql
CREATE TABLE departments(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL
)
```

### `ALWAYS`
ВСЕГДА АВТОМАТИЧЕСКИ ГЕНЕРИРУЕТ ЗНАЧЕНИЕ
```sql
CREATE TABLE departments(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL
)
```

### `TEXT`
ХРАНИТ ТЕКСТ БЕЗ ОГРАНИЧЕНИЯ ДЛИНЫ
```sql
CREATE TABLE employees(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    bio TEXT
)
```

### `VARCHAR`
ХРАНИТ ТЕКСТ С ОГРАНИЧЕННОЙ ДЛИНОЙ
```sql
CREATE TABLE users(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email VARCHAR(255),
    USERNAME VARCHAR(50)
)
```

### `CHAR`
ХРАНИТ СТРОКИ С ФИКСИРОВАННОЙ ДЛИНОЙ
```sql
CREATE TABLE countries(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    code CHAR(2),
    name TEXT NOT NULL
)
```

### `NUMERIC`
ТОЧНОЕ ЧИСЛО, ЗНАЧЕНИЕ ДО 10 СИМВОЛОВ
```sql
CREATE TABLE employees(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    salary NUMERIC(10,2)
)
```

### `DECIMAL`
ПОХОЖ НА NUMERIC, ЧАЩЕ ДЛЯ ДРОБНЫХ ЧИСЕЛ
```sql
CREATE TABLE products(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    price DECIMAL(10,2)
)
```

### `BOOLEAN`
ХРАНИТ TRUE OR FALSE
```sql
CREATE TABLE users(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
)
```

### `DATE`
ХРАНИТ ДАТУ БЕЗ ВРЕМЕНИ
```sql
CREATE TABLE employees(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    assigned_at DATE
)
```

### `TIME`
ХРАНИТ ОТМЕТКУ ВРЕМЕНИ
```sql
CREATE TABLE lessons(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL,
    start_time TIME,
    end_time TIME
)
```

### `TIMESTAMP`
ХРАНИТ ОТМЕТКУ ВРЕМЕНИ И ДАТУ '2026-05-20 18:35:00'
```sql
CREATE TABLE lessons(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT NOT NULL,
    start_time TIME,
    end_time TIME
)
```

### `ENUM`
ОГРАНИЧИВАЕТ ЗНАЧЕНИЕ ЗАДАННЫМ НАБОРОМ
```sql
CREATE TYPE order_status AS ENUM ('new', 'paid', 'shipped', 'cancelled')

CREATE TABLE orders(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    status_order order_status DEFAULT 'new'
)
```

### `NULL`
ОТСУТСТВИЕ ЗНАЧЕНИЯ
```sql
CREATE TABLE users(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name TEXT NOT NULL,
    middle_name TEXT
)
```


## 10. Условные выражения

### `CASE`
УСЛОВНАЯ ЛОГИКА ВНУТРИ SQL
```sql
SELECT name,
    salary,
    CASE 
        WHEN salary >= 15000 THEN 'high'
        WHEN salary >= 80000 THEN 'medium'
        ELSE 'low'
    END AS salary_level
FROM employees;
```

### `WHEN`
УСЛОВИЕ ВНУТРИ CASE
```sql
    CASE 
        WHEN salary >= 15000 THEN 'high'
        WHEN salary >= 80000 THEN 'medium'
        ELSE 'low'
    END AS salary_level
```

### `THEN`
УКАЗЫВАЕТ РЕЗУЛЬТАТ, ЕСЛИ УСЛОВИЕ ИСТИННО
```sql
SELECT name,
    salary,
    CASE 
        WHEN salary >= 15000 THEN 'high'
        WHEN salary >= 80000 THEN 'medium'
        ELSE 'low'
    END AS salary_level
FROM employees;
```

### `ELSE`
ЗАДАЕТ РЕЗУЛЬТАТ, ЕСЛИ ВСЕ УСЛОВИЯ НЕ ПОДОШЛИ
```sql
SELECT name,
    salary,
    CASE 
        WHEN salary >= 15000 THEN 'high'
        WHEN salary >= 80000 THEN 'medium'
        ELSE 'low'
    END AS salary_level
FROM employees;
```

### `COALESCE`
ВОЗВРАЩАЕТ ПЕРВОЕ ЗНАЧЕНИЕ, КОТОРОЕ НЕ ЯВЛЯЕТСЯ NULL
```sql
SELECT 
    name,
    COALESCE(salary, 0) as salary
FROM employees;
```
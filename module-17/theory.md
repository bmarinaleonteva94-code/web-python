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
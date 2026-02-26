logs = [
    ("ivan", 8), 
    ("ivan", 10),
    ("olga", 20),
    ("petr", 45),
]

hours_per_employee = {}
for employee, hours in logs:
    if employee in hours_per_employee:
        hours_per_employee[employee] += hours
    else:
        hours_per_employee[employee] = hours

print("Суммарные часы работы сотрудников: ")
for employee, hours in hours_per_employee.items():
    print(f" {employee}: {hours} часов ")

overtime = {}
underwork = {}

for employee, total_hours in hours_per_employee.items():
    if total_hours > 40:
        overtime[employee] = total_hours
    elif total_hours < 20:
        underwork[employee] = total_hours

print("Сотрудники с переработкой: ")
for employee, hours in overtime.items():
    print(f" {employee}: {hours} часов")

print("Сотрудники с недоработкой: ")
for employee, hours in underwork.items():
    print(f" {employee}: {hours} часов")
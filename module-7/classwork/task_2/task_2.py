"""
ЗАДАЧА: Умный контроль доступа (бейджи)

Даны записи содержащие журнал проходов сотрудников.

Каждая строка файла имеет формат:
дата,имя,действие

Где:
- дата     — строка в формате YYYY-MM-DD
- имя      — имя человека
- действие — ENTER (вход) или EXIT (выход)

Журнал проходов:
2026-02-01,Иван,ENTER
2026-02-01,Мария,ENTER
2026-02-01,Иван,EXIT
2026-02-01,Иван,EXIT
2026-02-01,Олег,EXIT
2026-02-02,Мария,EXIT
2026-02-02,Олег,ENTER

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Записать проходы в файл access.log

2. Прочитать файл access.log и загрузить данные.

3. Для каждого человека:
   - посчитать количество входов (ENTER)
   - посчитать количество выходов (EXIT)
   - определить, находится ли человек ВНУТРИ в конце лога
     (ENTER без последующего EXIT)

4. Найти людей с ошибками доступа:
   - EXIT без предварительного ENTER
   - два ENTER подряд без EXIT
   (сохранить таких людей в множество)

5. Для каждой даты посчитать количество входов (ENTER).

6. Найти дату с максимальным количеством входов.

7. Записать подробный отчёт в файл access_report.txt.
"""
access_list = '''2026-02-01,Иван,ENTER
2026-02-01,Мария,ENTER
2026-02-01,Иван,EXIT
2026-02-01,Иван,EXIT
2026-02-01,Олег,EXIT
2026-02-02,Мария,EXIT
2026-02-02,Олег,ENTER
'''

with open ("access.log", "w", encoding="utf-8") as f:
    f.write(access_list)

events = []

stats = {}
inside = {}
errors = set()
daily_enters = {}

with open ("access.log", "r", encoding="utf-8") as f:
    for line in f:
        date, name, action = line.strip().split(",")
        events.append((date, name, action))

for date, name, action in events:
    stats.setdefault(name, {"ENTER" : 0, "EXIT": 0})
    inside.setdefault(name, False)
    daily_enters.setdefault(date, 0)

    if action == "ENTER":
        if inside[name]:
            errors.add(name)
        inside[name] = True
        stats[name]["ENTER"] += 1
        daily_enters[date] += 1
    else:
        if not inside[name]:
            errors.add(name)
        inside[name] = False
        stats[name]["EXIT"] += 1
    max_day = None
    max_enters = 0
    for date, count in daily_enters.items():
        if count > max_enters:
            max_day = date
            max_enters = count            
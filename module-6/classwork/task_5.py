import random
tasks = []
for i in range(10):
    tasks.append({
        "id": f"t_{i}",
        "assignee": random.choice(["ivan", "olga", "petr", "anna", "oleg"]),
        "status": random.choice(["in progress", "blocked", "in review", "waiting vendor"]),
        "days_in_status": random.randint(0, 10)
    })
executor = set()
for task in tasks:
    if task["status"] == "in progress" and task["days_in_status"] > 7:
        executor.add(task["assignee"])

status_assignes = {}
for task in tasks:
    status = task["status"]
    assignee = task["assignee"]
    if status not in status_assignes:
        status_assignes[status] = set()
    status_assignes[status].add(assignee)
result = {}
for status in status_assignes:
    if len(status_assignes[status]) == 1:
        result[status] = list(status_assignes[status])[0]

max_days = 0
assignee = None
for task in tasks:
    if task["status"] == "in progress" or task["status"] == "blocked":
        if task["days_in_status"] > max_days:
            max_days = task["days_in_status"]
            assignee = task["assignee"]

print(f"{assignee}: {max_days}")
print(result)
print(executor)
print(tasks)
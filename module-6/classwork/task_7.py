history = [
    ("t_1", "new"),
    ("t_1", "in progress"),
    ("t_1", "done"),
    ("t_2", "new"), 
    ("t_2", "done"),
    ("t_3", "new"),
    ("t_3", "in progress"),
    ("t_3", "cancelled"),
    ("t_4", "new"),
    ("t_4", "cancelled"),
    ("t_4", "done")
]

allowed = {
    ("new", "in progress"),
    ("in progress", "done"),
    ("new", "cancelled"), 
    ("in progress", "cancelled")
}
last_status = {}
errors = {}
for entity, status in history:
    last_status[entity] = status
    continue
prev = last_status[entity]
if (prev, status) not in allowed:
    if entity not in errors:
        errors[entity] = (prev, status)
else:
    last_status[entity] = status

for entity, transition in errors.items():
    print(entity, ":", transition)
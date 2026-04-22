logs = [
    ("ivan", "d1", "login"),
    ("ivan", "d1", "view"),
    ("ivan", "d2", "login"),
    ("olga", "d1", "login"), 
    ("petr", "d2", "error"),
    ("anna", "d1", "login"),
    ("anna", "d2", "view")
]

user_actions_count = {}
user_action = {}
user_days = {}
day_activity = {}
for user, day, action in logs:
    user_actions_count[user] = user_actions_count.get(user, 0) + 1
    if user not in user_action:
        user_action[user] = set()
    user_action[user].add(action)
    if user not in user_days:
        user_days[user] = set()
    user_days[user].add(day)
    day_activity[day] = day_activity.get(day, 0) + 1   

user_with_error = set()
for user, actions in user_action.items():
    if "error" in actions and "login" not in actions:
        user_with_error.add(user)
    
active_multi_day_users = set()
for user, days in user_days.items():
    if len(days) > 1:
        active_multi_day_users.add(user)



print(user_actions_count)
print(user_with_error)   
print(active_multi_day_users)
payments = [
    ("ivan", 100),
    ("ivan", -30),
    ("ivan", -20),
    ("olga", 200),
    ("petr", -50),
]

balance = {}
negative_balance = {}
operation_count = {}

for user, amount in payments:
    if user in balance:
        balance[user] += amount 
    else:
        balance[user] = amount
    
    operation_count[user] = operation_count.get(user, 0) +1

print("Баланс каждого пользователя: ")
for user, amount in balance.items():
    print(f" {user}: {amount}")
    if amount < 0:
        negative_balance[user] = amount

print("Пользователи с отрицательным балансом: ")
for user, balance in negative_balance.items():
    print(f"{user}: {balance}")

print("Пользователи с операциями > 2: ")
for user, quantity in operation_count.items():
    if operation_count[user] > 2:
        print(f"{user}: {balance}")
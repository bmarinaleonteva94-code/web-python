purchases = [
    {"user": "Алиса", "items": ["яблоко", "банан"],          "price": 120, "timestamp": 1},
    {"user": "Боб",   "items": ["банан"],                    "price": 50,  "timestamp": 2},
    {"user": "Алиса", "items": ["апельсин", "яблоко"],       "price": 150, "timestamp": 5},
    {"user": "Боб",   "items": ["яблоко", "апельсин"],       "price": 130, "timestamp": 6},
    {"user": "Алиса", "items": ["банан", "банан"],           "price": 70,  "timestamp": 15},
    {"user": "Боб",   "items": ["банан"],                    "price": 40,  "timestamp": 25},
]

purchase_count = {}
purchase_amount = {}
user_unique_items = {}
total_items = {}
item_counts = {}
user_timestamps = {}
max_gaps = {}

for purchase in purchases:
    user = purchase['user']
    if user in purchase_count:
        purchase_count[user] += 1
    else:
        purchase_count[user] = 1

    price = purchase['price']
    if user in purchase_amount:
        purchase_amount[user] += price
    else:
        purchase_amount[user] = price

    items = purchase['items']
    if user in user_unique_items:
        user_unique_items[user].update(items)
    else:
        user_unique_items[user] = set(items)

    items_count = len(purchase["items"])
    if user in total_items:
        total_items[user] += items_count
    else:
        total_items[user] = items_count
   
    for item in purchase['items']:
        item_counts[item] = item_counts.get(item, 0) + 1

    if user in user_timestamps:
        user_timestamps[user].append(purchase['timestamp'])
    else:
        user_timestamps[user] = [purchase['timestamp']]

    for item in purchase['items']:
        item_counts[item] = item_counts.get(item, 0) + 1

most_popular_item = None
max_count = 0
for item, count in item_counts.items():
    if count > max_count:
        max_count = count
        most_popular_item = item

max_money = -1
winner_name = ""
for user, amount in purchase_amount.items():
    if amount > max_money:
        max_money = amount
        winner_name = user

max_items = -1
winner_items = ""
for user, total in total_items.items():
    if total > max_items:
        max_items = total
        winner_items = user

for user, timestamps in user_timestamps.items():
    sorted_timestamps = sorted(timestamps)

    if len(sorted_timestamps) < 2:
        max_gaps[user] = 0
    else:
        gaps = []
        for i in range(1, len(sorted_timestamps)):
            gap = sorted_timestamps[i] - sorted_timestamps[i-1]
            gaps.append(gap)
        max_gaps[user] = max(gaps)

print("Количество покупок каждого пользователя: ")
for user, count in purchase_count.items():
    print(f"{user}: {count}")

print("Сумма потраченных денег пользователей: ")
for user, amount in purchase_amount.items():
    print(f"{user}: {amount}")

print("Список уникальных товаров каждого пользователя: ")
for user, items in user_unique_items.items():
    items_str = ", ".join(items)
    print(f"{user}: {items_str}")

print("Общее количество покупок пользователя: ")
for user, total in total_items.items():
    print(f"{user}: {total}")

print(f"Товар, который покупали чаще всего: {most_popular_item}")

print(f"Пользователь, потративший больше всего денег: {winner_name}")

print(f"Пользователь, купивший больше всего: {winner_items}")

print("Самый большой перерыв между покупками для каждого пользователя: ")
for user, gap in max_gaps.items():
    if gap == 1:
        print(f"Пользователь {user} совершил только одну покупку")
    else:
        print(f"{user}: {gap}")
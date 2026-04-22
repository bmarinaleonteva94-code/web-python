numbers = (1,2,3,4,33,4,222,11,2,333,32)

stats = {}

for num in numbers:
    length = len(str(abs(num)))
    stats[length] = stats.get(length, 0) +1
for digits, count in sorted(stats.items()):
    print(f"Количество {digits}-значных чисел: {count}")
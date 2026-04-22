quantity = int(input("Введите количество пар \"ключ = значение\": "))
dict = {}
print(f"Введите значения для пар \"ключ = значение\": ")
for i in range(quantity):
    key = input(f"Введите значение ключа для пары {i+1}: ")
    value = input(f"Введите значение для ключа \"{key}\": ")
    dict[key] = value
print(dict)
"""
ЗАДАЧА: Учёт инвентаря на складе

Формат строки:
дата,товар,тип,количество

Операции:
2024-01-01,яблоко,IN,50
2024-01-02,банан,IN,30
2024-01-03,яблоко,OUT,10
2024-01-03,груша,OUT,5
2024-01-04,груша,IN,20
2024-01-05,банан,OUT,40
2024-01-06,яблоко,OUT,5

Типы операций:
- IN  : поступление товара
- OUT : отгрузка товара

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Создать файл inventory.txt с операциями склада

2. Прочитать файл и загрузить все операции.

3. Для каждого товара:
   - посчитать итоговое количество на складе
   - посчитать общее количество поступивших единиц
   - посчитать общее количество отгруженных единиц

4. Найти товары:
   - у которых итоговое количество < 0 (ошибка учёта)
   - которые ни разу не поступали, но отгружались

5. Найти товар с:
   - максимальным количеством поступлений
   - максимальным количеством отгрузок

6. Сформировать множество всех дат,
   когда происходили операции с товаром "яблоко".

7. Записать подробный отчёт в файл report.txt.

- ОТЧЁТ ПО СКЛАДУ
- Итоговые остатки
- Общее поступление
- Общая отгрузка
- Товары с отрицательным остатком:
- Товары без поступлений, но с отгрузкой:
- Товар с максимальным поступлением:
- Товар с максимальной отгрузкой:
- Даты операций с яблоком:
"""
operations = '''2024-01-01,яблоко,IN,50
2024-01-02,банан,IN,30
2024-01-03,яблоко,OUT,10
2024-01-03,груша,OUT,5
2024-01-04,груша,OUT,20
2024-01-05,банан,OUT,40
2024-01-06,яблоко,OUT,5'''

with open ("inventory.txt", "w", encoding="utf-8") as f:
   f.write(operations)

operations = []

with open("inventory.txt", "r", encoding="utf-8") as f:
   for line in f:
      date, product, operation_type, quantity = line.strip().split(",")
      operations.append({ "date": date, "product": product, "operation_type": operation_type, "quantity": int(quantity)})

total_count = {}
total_in = {}
total_out = {}
product_dates = {}

for operation in operations:
   date, product, operation_type, quantity = operation["date"], operation["product"], operation["operation_type"], operation["quantity"]

   total_count.setdefault(product, 0)
   total_in.setdefault(product, 0)
   total_out.setdefault(product, 0)

   product_dates.setdefault(product, set()).add(date)

   if operation_type == "IN":
      total_count[product] += quantity
      total_in[product] += quantity

   else:
      total_count[product] -=quantity
      total_out[product] += quantity

negative_products = []
for product, quantity in total_count.items():
   if total_count[product] < 0: 
      negative_products.append(product)
   

max_in_product = None
max_in_quantity = -1

for product, quantity in total_in.items():
   if quantity > max_in_quantity:
      max_in_product = product
      max_in_quantity = quantity
print(f"Товары с максимальным количеством поступлений: \n  {max_in_product}: {max_in_quantity}")
max_out_product = None
max_out_quantity = -1
for product, quantity in total_out.items():
   if quantity > max_out_quantity:
      max_out_product = product
      max_out_quantity = quantity
print(f"Товары с максимальным количеством отгрузок: \n  {max_out_product}: {max_out_quantity}")

no_in_but_out = []
for key, value in total_count.items():
   if total_in[key] == 0 and total_out[key] > 0 :
      no_in_but_out.append(key)
   print(f"На складе {key}: {value}")
print(no_in_but_out)

print("-"*20)
for key, value in total_in.items():
   print(f"Приехало {key}: {value}")
print("-"*20)
for key, value in total_out.items():
   print(f"Отгружено {key}: {value}")    

print(product_dates.get("яблоко", set()))

with open ("report.txt", "w", encoding="utf-8") as f:
   f.write("               ОТЧЁТ ПО СКЛАДУ          \n ")

   f.write("    Итоговые остатки: \n")
   for product, quantity in total_count.items():
        f.write(f"  {product}: {quantity} \n")
   f.write("\n")

   f.write("    Общее поступление: \n")
   for product, quantity in total_in.items():
      f.write(f"  {product}: {quantity}\n")
   f.write("\n")

   f.write("    Общая отгрузка: \n")
   for product, quantity in total_out.items():
      f.write(f"  {product}: {quantity}\n")
   f.write("\n")

   f.write("    Товары с отрицательным остатком: \n")
   for product in negative_products:
      f.write(f"{product}: {total_count[product]} \n")
   f.write("\n")

   f.write("    Товары без поступлений, но с отгрузкой: \n")
   f.write(f"{no_in_but_out} \n")
   f.write("\n")

   f.write("    Товар с максимальным поступлением: \n")
   f.write(f"{max_in_product}: {max_in_quantity} \n")
   f.write("\n")

   f.write("    Товар с максимальной отгрузкой: \n")
   f.write(f"{max_out_product}: {max_out_quantity} \n")
   f.write("\n")

   f.write("    Даты операций с яблоком: \n")
   apple_dates = product_dates.get("яблоко", set())
   for date in apple_dates:
      f.write(f"{date} \n")
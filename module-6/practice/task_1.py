fruits = ("яблоко", "апельсин", "банан", "яблокогруша", "яблоко")
fruit = input("Введите название фрукта: ")
quantity = fruits.count(fruit)
print(quantity)

count_fruit = 0
for i in fruits:
    if fruit in i:
        count_fruit +=1
print(count_fruit)
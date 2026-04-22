# my_set_1 = set([1,2,3,4,5,5])
# print(my_set_1)

# my_set = {1,1,2,3,1}
# print(my_set)

# letters = set("hello")
# print(letters)

# set_tuple = set((1,2,3,4,5,3,2))
# print(set_tuple)

# my_set = {x for x in range(5)}      # генератор множеств
# print(my_set)

# # добавление элементов в множество
# fruits = {"Яблоко", "Банан", "апельсин"}
# fruits.add("pear")
# fruits.update(["blackberry", "lemon"])
# print(fruits)

# # удаление элементов
# fruits.remove("Яблоко")
# fruits.discard("pear")
# fruits.pop()        # удаляет рандомный элемент
# print(fruits)

# операции над множествами
# 1. объединение
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
# result = set_a.union(set_b)
# result_operator = set_a | set_b
# set_a |= set_b      # присвоение set_a значение set_b
# print(result, result_operator)

# 2. пересечение(какие элементы есть и в первом, и во втором множествах)
# result1 = set_a.intersection(set_b)
# result_operator1 = set_a & set_b
# set_a &= set_b
# print(result1, result_operator1, set_a)

# # 3. Paзность
# result = set_a.difference(set_b)
# result_operator = set_a - set_b
# set_a -=set_b
# print(set_a, result, result_operator)

# # 4. симметрическая разность
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# result = set1.symmetric_difference(set2)
# result_operator = set1 ^ set2
# set1 ^= set2
# print(set1, result, result_operator)

my_set = {1,2,3}
print(3 in my_set)
print(5 not in my_set)
print(len(my_set))
print(sum(my_set))     # только для чисел
print(min(my_set), max(my_set))

for num in my_set:          # итерация по множеству
    print(num)         
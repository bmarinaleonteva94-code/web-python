# my_list = [1,2,3, True]
# my_list1 = [[1,2], [3,4]]
# print (my_list)
# print(len(my_list))
# print(my_list[2])
# print(len(my_list1))

# numbers = [1,2,3,4,5]
# total = sum(numbers)
# print(total)

# maximum = max(numbers)
# minimum = min(numbers)
# print(maximum, minimum)



# numbers = [3,66,7,9,2,44,5]
# sorted_nums = sorted(numbers)
# sorted_nums1 = sorted(numbers, reverse=True)
# print(sorted_nums)
# print(sorted_nums1)

# rev = reversed(numbers)
# print(list(rev))

# fruits = ['apple', 'cherry', 'banana']
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")

# num = ['1','2','3','6']
# num1 = [1,2,3]
# s = list(map(lambda x: x**2, num1))
# s1 = list(map(int, num))
# print(s)
# print(s1)

# def double():
#     return num1*2
# list_double = list(map(double, s))
# print(list_double)
# def filter_func(num): 
#     return num % 2 == 0
# numbers = [1,2,3,4,5,6,7,8,9,10]
# evens = list(filter(lambda x: x % 2 ==0, numbers))
# evens1 = list(filter(filter_func, numbers))
# print(evens, evens1)


# words = ['paper', 'tomato', 'apple']
# result = ','.join(words)
# print(result)


# my_list = ['apple', 'ban', 2]
# my_list.append(4)     # добавляет новый элемент в список  
# my_list.extend([5,6])
# my_list.extend('apple')   #разбивает слово на отдельные элементы
# print(my_list)

# my_list1 = ['banana', 3, 'a']
# new_list = my_list + my_list1    
# print(new_list)

# my_list.insert(1,'code')   #добавляет новый элемент code после элемента с индексом 0

# my_list.remove(2)

# my_list.pop()  #удаляет последний элемент
# my_list.pop(1)  #удаляет элемент с индексом 1

# my_list.clear()

# print(my_list)


# my_list = [5,6,7,32,44,5,5,55]
# count = my_list.count(5)
# print(count)

# my_list.sort()
# # my_list.sort(reverse=True)
# my_list.reverse()
# print(my_list)


# my_list = [1,2,3,-4,-5,6,7,8,9,10]
# print(my_list[0:5])     #print(my_list[start:end:step])   выводит элементы с индекса 0 до индекса 5
# print(my_list[0:6:2])      # шаг 2: выведет 1, 3,5
# print(my_list[:6])   # с начала до индекса 6    my_list[3:]   с индекса 3 до конца
# print(my_list[:])   #копирует my_list
# print(my_list[-1])
# print(my_list[::-1])   #разворачивает список

# res = [x**2 for x in my_list]   #генератор, то же самое, что и запись ниже

# result = []
# for x in my_list:
#     result.append(x**2)
# print(res, result)

# res = [x**2 for x in my_list if x%2==0]
# print(res)

# res1 = [0 if x<0 else x for x in my_list]
# print(res1)


# text = "    python, 123   "
# print(text[0:7])
# print(text[0:3])   #обрезает строку с индекса 0 до индекса 3
# print(text[::-1])   #разворачивает слово

# print(text.upper())   #заглавные буквы
# print(text.lower())    #строчные буквы
# print(text.capitalize())   #начальная в заглавную
# print(text.swapcase())     #меняет регистр на обратный

# print(text.find("p"))    #поиск индекса элемента, если не найдет - вернет -1
# print(text.index("p"))   #поиск индекса элемента, если такого элемента нет - выдает ошибку
# #print(text.index("k"))

# print(text.replace("pyt", "213"))   # заменяет "pyt" на "213", text('pyt', '123', 2)   - заменяет у 2 найденных элементов "pyt"
# print("Только буквы: ", text.isalpha())    # если только буквы -True
# print("Только цифры: ", text.isdigit())
# print("Только буквы и цифры: ", text.isalnum())
# print("Пробелы: ", text.isspace())
# print("Только заглавные буквы: ", text.isupper())
# print("Только строчные буквы: ", text.islower())
# print(text.strip())    # убирает пробелы по краям строки
# print(text.strip("*"))
# print(text.lstrip())    # убирает пробелы слева
# print(text.rstrip())     #  убирает пробелы справа

# print(text.split())   # разбивает строку по пробелам
# f = text.split(", ")   
# u = ", ".join(f)
# print(f, u)
# sl = text.splitlines()
# print(sl)


# tuple_1 = (1,2,3)     #кортеж, не изменяемый, нельзя менять длину
# tuple_1_sym = ("b")
# tuple_2_sym = ("b",)
# print(tuple_1_sym, tuple_2_sym)
# tuple_2 = tuple([1,2,3])
# tuple_2_1 = tuple(range(0, 11))
# tuple_3 = 1,2,3
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print(tuple_2_1[0])
# print(tuple_2_1[2:5])

# num1, *other, last_el = tuple(range(0,11))
# print(num1, other, last_el)


# tuple1 = (1,2)
# tuple2 = (3,4)       # объединение 2 кортежей
# result = tuple1 + tuple2
# print(result)

# pattern = ("a", "b")                           #повторение символов кортежа на определенное количество раз
# repeated = pattern * 2
# print(repeated)

# f = ("apple", "banana")
# print("apple" in f)      # принадлежность


# # методы кортежей
# numbers = (1,2,3,2,2,5,6)
# print(numbers.count(2))    #ищет элемент и считает его количество
# print(numbers.index(2))    # индекс первого найденного элемента

# num_tuple = tuple(range(0,5))
# for num in num_tuple:
#     print(num)

# for index, num in enumerate(num_tuple):    #возвращает индекс и элемент
#     print(index, num)
# def func_1():
#     print("Функция")
# func_1()

# def func_2():
#     return "Привет func_2"
# print(func_2())

# def func_3():
#     pass           # для предотвращения ошибок, позволяет не дописывать функцию

# def func_4(name):
#     print(f"{name}")    
# func_4("Марина")

# def func_4_1(name, age, city):
#     print(f"{name} - {age} - {city}")
# func_4_1("Павел", "24", "Чебоксары")     # или func_4_1(name="Павел", age = 24, city = "Чебоксары")

# def func_5(*args):
#     print(args)
# func_5(1,2,3,4,5)

# def func_6(*args):
#     total = 0
#     for num in args:
#         total += num    # собирает в один кортеж
#     print(total)
# func_6(1,2,3,4,5)

# def func_7(**kwargs):
#     print(kwargs)          # собирает в словарь {'name': 1, 'age': 2}
# func_7(name=1, age=2)

# def func_8(num1, num2, *args, **kwargs):
#     print(f"{num1}, {num2}")
#     print(args)
#     print(kwargs)
# func_8(1,2,3,4,5, name=6)

# def func_9(obj):
#     print(obj)
# func_9({"a":1, "b":2})



# def func_1():
#     result = []
#     for i in range(5):
#         result.append(i)        # обычная функция
#     return result
# print(func_1())

# def func_2():
#     for i in range(5):
#         yield i            # генератор
# gen = func_2()
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for i in func_2():
#     print(i)


# рекурсия
def factorial(n):
    if n<=1:       # базовый случай
        return 1
    return n * factorial(n-1)             # рекурсивный шаг
print(factorial(9))   
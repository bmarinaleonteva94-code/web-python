#  в файле .gitignor записать:
#          venv
#          venv/
#          /venv

# python -m venv venv  или python3 -m venv venv или   py -m venv venv
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# .\venv\Scripts\Activate.ps1


# print ("123", "hello", sep="#", end="\n")   # sep="#" заменяет пробел между двумя строка на #    \n перенос следующей строки на новую строку
# print("Проверка переноса")

# num = 0
# txt = "Текст"
# print(num, txt)
# print(f"Привет, {txt}")

# text_str = input("Введите текст: ")
# print(text_str)

# num = int(input("Введите число: "))   # int - целое число   float - число с плавающей точкой
# print(num, num*2)
# print(num**3)     #  x**y - возведение числа x в степень y
# print(num//2)    #   // - целочисленное деление

# min_num = min(2,4,5,66,5)   # min - выводит минимальное число   max - максимальное число
# max_num = max(22,3,55,3,9)
# print(min_num, max_num)

# age = int(input("Введите ваш возраст: "))
# access = True
# if age<18:
#     print("no")
# elif age>18 and age<30:
#     print("ok")
# else:
#     print("yes")

# day = "Суббота"
# if day == "Суббота" or day == "Воскресенье":
#     print("Выходной")
# else:
#     print("Будни")

# is_running_pc = False
# if not is_running_pc:
#     print("Выключен")
# else:
#     print("Включен")

# for item in range(5):
#     print(item)

# for item1 in range (2,20,2):     # от 2 до 19 с шагом в 2
#     print(item1)

# text_str = "hello"
# for i in text_str:      # выводит каждую букву на новой строке
#     print(i)

# while True:
#     input_str = input("Введите 'выход' для выхода из цикла ")
#     if input_str == "выход":                     # выводит набранную строку до выхода из цикла, при наборе "выход" цикл заканчивается
#         break
#     print(input_str)

while True:
    print("===Меню===")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Выход")
    option_str = input("Выберите опцию (1-3) ")
    if option_str == "1":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print(f"Результат: {a+b}")
    elif option_str == "2":
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        print(f"Результат: {a-b}")
    elif option_str == "3":
        print("Выход из программы")
        break
    else:
        print("Неверная опция ")
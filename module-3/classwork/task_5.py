str = input("Введите любую строку: ")
count_letters = 0
count_digit = 0
for char in str:
    if char.isalpha():
        count_letters += 1
    elif char.isdigit():
        count_digit += 1
print(f"Количество букв в строке: {count_letters}")
print(f"Количество цифр в строке: {count_digit}")
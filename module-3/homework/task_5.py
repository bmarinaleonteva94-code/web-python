numbers = [2,3,4,5,6,-2,-1,0,0,33]
maximum = max(numbers)
minimum = min(numbers)
negative_numbers = 0
positive_numbers = 0
zero_numbers = 0
for number in numbers:
    if number < 0:
        negative_numbers +=1
    elif number > 0:
        positive_numbers +=1
    else:
        zero_numbers +=1
print(f'Максимальное число в списке: {maximum}')
print(f'Минимальное число число в списке: {minimum}')
print(f'Количество положительных чисел: {positive_numbers}')
print(f'Количество отрицательных чисел: {negative_numbers}')
print(f'Количество нулей: {zero_numbers}')




numbers1 = input("Введите любое количество целых чисел через пробел: ")
numbers_list = list(map(int, numbers1.split()))
maximum1 = max(numbers_list)
minimum1 = min(numbers_list)
negative_numbers1 = 0
positive_numbers1 = 0
zero_numbers1 = 0
for number in numbers_list:
    if number < 0:
        negative_numbers1 +=1
    elif number > 0:
        positive_numbers1 +=1
    else:
        zero_numbers1 +=1
print(f'Максимальное число в списке: {maximum1}')
print(f'Минимальное число число в списке: {minimum1}')
print(f'Количество положительных чисел: {positive_numbers1}')
print(f'Количество отрицательных чисел: {negative_numbers1}')
print(f'Количество нулей: {zero_numbers1}')
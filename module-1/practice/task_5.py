num = int(input("Введите четырехзначное число: "))
num1 = num // 1000     
num2 = num //100 % 10
num3 = num // 10 %10
num4 = num %10
print(f"{num4}{num3}{num2}{num1}")
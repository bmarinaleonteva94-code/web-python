text = input('Введите арифметическое выражение в формате "число операция число": ')
if "+" in text:
    a, b = text.split("+")
    result = float(a) + float(b)
elif "-" in text:
    a, b = text.split("-")
    result = float(a) - float(b)
elif "*" in text:
    a, b = text.split("*")
    result = float(a) * float(b)
else:
    a, b = text.split("/")
    if float(b) == 0:
        print("Деление на ноль невозможно")
        exit()
    else:
        result = float(a) / float(b)
print(f"{text}={result}")
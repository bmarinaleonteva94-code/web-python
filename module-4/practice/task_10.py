a = int(input("Введите первое число: "))
b = int(input("введите второе число: "))
def sum(a,b):
    if a == b:
        return a
    return a + sum(a+1, b)
print(sum(a,b))
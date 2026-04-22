star_number = int(input("Введите количество звезд: "))
def star(n):
    if n ==1:
        return "*"
    return "*" + star(n-1)
print(star(star_number))
    
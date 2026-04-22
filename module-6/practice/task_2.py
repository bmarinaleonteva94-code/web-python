car_manufacturers = ("lada", "lada", "renault", "bmw")
car_name = input("Введите название производителя: ")
replacement = input("Слово для замены: ")
new_car_manufactures = list(car_manufacturers)
for i in range(len(new_car_manufactures)):
    if new_car_manufactures[i] == car_name:
        new_car_manufactures[i] = replacement
new_list = tuple(new_car_manufactures)
print(new_list)
employees = {}

def load_employees():
    try:
        with open("employees.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line: 
                    continue
                parts = line.split("|")
                if len(parts) == 7:
                    emp_id = parts[0]
                    employees[emp_id] = {
                        "full_name": parts[1],
                        "phone": parts[2],
                        "email": parts[3],
                        "position": parts[4],
                        "room_number": parts[5],
                        "age": int(parts[6])
                    }
        print("Данные сотрудников загружены.")
    except FileNotFoundError:
        print("Файл employees.txt не найден. Создан новый список.")

def save_employees():
    with open("employees.txt", "w", encoding="utf-8") as f:
        for emp_id, emp in employees.items():
            line = f"{emp_id}|{emp['full_name']}|{emp['phone']}|{emp['email']}|{emp['position']}|{emp['room_number']}|{emp['age']}\n"
            f.write(line)
    print("Данные сохранены в файл.")

def add_employee(emp_id, full_name, phone, email, position, room_number, age):
    if emp_id in employees:
        print(f"Сотрудник с ID {emp_id} уже существует.")
        return

    employees[emp_id] = {
        "full_name": full_name,
        "phone": phone,
        "email": email,
        "position": position,
        "room_number": room_number,
        "age": age
    }
    print(f"Сотрудник {full_name} (ID: {emp_id}) добавлен.")

def remove_employee(emp_id):
    if emp_id in employees:
        full_name = employees[emp_id]["full_name"]
        del employees[emp_id]
        print(f"Сотрудник {full_name} (ID: {emp_id}) удалён.")
    else:
        print(f"Сотрудник с ID {emp_id} не найден.")

def find_employee_by_lastname(lastname):
    found = []
    for emp_id, emp in employees.items():
        if lastname.lower() in emp["full_name"].lower():
            found.append((emp_id, emp))
        if found:
            print(f"Сотрудники с фамилией '{lastname}': ")
            for emp_id, emp in found:
                print(f"ID: {emp_id} | ФИО: {emp["full_name"]} | Возраст: {emp["age"]} | Должность: {emp["position"]}")
        else:
            print(f"Сотрудники с фамилией {lastname} не найден.")

def find_employees_by_age(age):
    found = []
    for emp_id, emp in employees.items():
        if emp["age"] == age:
            found.append((emp_id, emp))
    if found:
        print(f"Сотрудники возраста {age} лет: ")
        for emp_id, emp in found:
            print(f"ID: {emp_id} | ФИО: {emp['full_name']} | Должность: {emp['position']} | Кабинет: {emp['room_number']}")
    else:
        print(f"Сотрудники возраста {age} лет не найдены")
    return found

def find_employees_by_letter(letter):
    found = []
    for emp_id, emp in employees.items():
        if emp["full_name"].lower().startswith(letter.lower()):
            found.append((emp_id, emp))

    if found:
        print(f"\nСотрудники, фамилия которых начинается на '{letter}':")
        for emp_id, emp in found:
            print(f"ID: {emp_id} | ФИО: {emp['full_name']} | Возраст: {emp['age']} | Должность: {emp['position']}")
    else:
        print(f"Сотрудники с фамилией на букву '{letter}' не найдены.")
    return found

def save_found_employees(found_list):
    if not found_list:
        print("Нет данных для сохранения.")
        return

    with open("employees_found", "w", encoding="utf-8") as f:
        for emp_id, emp in found_list:
            line = f"ID: {emp_id}, ФИО: {emp['full_name']}, Возраст: {emp['age']}, Должность: {emp['position']}\n"
            f.write(line)
    print(f"Найденная информация сохранена в файл 'employees_found'.")

def update_employee(emp_id, full_name=None, phone=None, email=None,
                   position=None, room_number=None, age=None):
    if emp_id not in employees:
        print(f"Сотрудник с ID {emp_id} не найден.")
        return

    emp = employees[emp_id]
    if full_name is not None:
        emp["full_name"] = full_name
    if phone is not None:
        emp["phone"] = phone
    if email is not None:
        emp["email"] = email
    if position is not None:
        emp["position"] = position
    if room_number is not None:
        emp["room_number"] = room_number
    if age is not None:
        emp["age"] = age

    print(f"Данные сотрудника {emp_id} обновлены.")

def show_all_employees():
    if not employees:
        print("Список сотрудников пуст.")
        return

    print("\nВсе сотрудники:")
    for emp_id, emp in employees.items():
        print(f"ID: {emp_id} | ФИО: {emp['full_name']} | Должность: {emp['position']} | Кабинет: {emp['room_number']}")

def main():
    load_employees() 

    print("Доступные команды (введите цифру от 1 до 6):")
    print("1. Добавить сотрудника")
    print("2. Удалить сотрудника")
    print("3. Найти сотрудника по фамилии")
    print("4. Найти сотрудников указанного возраста")
    print("5. Найти сотрудников по первой букве фамилии")
    print("6. Показать всех сотрудников")
    print("7. Обновить данные сотрудника")
    print("8. Сохранить все данные в файл")
    print("9. Выход")
   
    while True:
        command = input("\nВведите команду: ").strip()
        if not command:
            continue

        action = command.lower()

        if action == "9":
            save_employees() 
            print("До свидания!")
            break

        elif action == "1":
            emp_id = input("Введите ID сотрудника: ")
            full_name = input("Введите имя сотрудника: ")
            try:
                phone = int(input("Введите телефон сотрудника: "))
            except ValueError:
                print("Ошибка: телефон должен быть числом.")
                continue
            email = input("Введите email сотрудника: ")
            position = input("Введите должность сотрудника: ")
            room_number = input("Введите номер кабинета: ")
            age = input("Введите возраст сотрудника: ")
            add_employee(emp_id, full_name, phone, email, position, room_number, age)

        elif action == "2":
            emp_id = input("Введите ID сотрудника, которого необходимо удалить: ")
            remove_employee(emp_id)

        elif action == "3":
            lastname = input("Введите фамилию: ")
            found = find_employee_by_lastname(lastname)
            if found:
                save_found_employees(found)

        elif command == "4":
            try:
                age = int(input("Введите возраст для поиска: "))
            except ValueError:
                print("Ошибка: возраст должен быть числом.")
                continue
            found = find_employees_by_age(age)
            if found:
                save_found_employees(found)

        elif command == "5":
            letter = input("Введите первую букву фамилии для поиска: ").strip()
            if not letter:
                print("Буква не может быть пустой.")
                continue
            found = find_employees_by_letter(letter)
            if found:
                save_found_employees(found)

        elif action == "6":
            show_all_employees()

        elif action == "7":
            emp_id = input("Введите ID сотрудника: ")
            if emp_id not in employees:
                print(f"Сотрудник с ID {emp_id} не найден.")
                continue

            print("Оставьте поле пустым, если не нужно менять.")
            full_name = input("Новое имя: ") or None
            try:
                phone_input = input("Новый телефон: ")
                phone = int(phone_input) if phone_input else None
            except ValueError:
                print("Ошибка: телефон должен быть числом.")
                continue
            email = input("Новый email: ") or None
            position = input("Новая должность: ") or None
            room_number = input("Новый номер кабинета: ") or None
            age = input("Новый возраст: ") or None

            update_employee(emp_id, full_name, phone, email, position, room_number, age)

        elif command == "8":
            save_employees()

        else:
            print("Неверная команда. Введите число от 1 до 9.")

main()
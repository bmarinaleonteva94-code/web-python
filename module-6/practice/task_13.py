employees = {}


def add_employee(emp_id, full_name, phone, email, position, room_number, skype):
    if emp_id in employees:
        print(f"Сотрудник с ID {emp_id} уже существует.")
        return

    employees[emp_id] = {
        "full_name": full_name,
        "phone": phone,
        "email": email,
        "position": position,
        "room_number": room_number,
        "skype": skype
    }
    print(f"Сотрудник {full_name} (ID: {emp_id}) добавлен.")

def remove_employee(emp_id):
    if emp_id in employees:
        full_name = employees[emp_id]["full_name"]
        del employees[emp_id]
        print(f"Сотрудник {full_name} (ID: {emp_id}) удалён.")
    else:
        print(f"Сотрудник с ID {emp_id} не найден.")

def find_employee(emp_id):
    if emp_id in employees:
        emp = employees[emp_id]
        print(f"\nДанные сотрудника (ID: {emp_id}):")
        print(f"  ФИО: {emp['full_name']}")
        print(f"  Телефон: {emp['phone']}")
        print(f"  Email: {emp['email']}")
        print(f"  Должность: {emp['position']}")
        print(f"  Кабинет: {emp['room_number']}")
        print(f"  Skype: {emp['skype']}")
    else:
        print(f"Сотрудник с ID {emp_id} не найден.")

def update_employee(emp_id, full_name=None, phone=None, email=None,
                   position=None, room_number=None, skype=None):
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
    if skype is not None:
        emp["skype"] = skype

    print(f"Данные сотрудника {emp_id} обновлены.")

def show_all_employees():
    if not employees:
        print("Список сотрудников пуст.")
        return

    print("\nВсе сотрудники:")
    for emp_id, emp in employees.items():
        print(f"ID: {emp_id} | ФИО: {emp['full_name']} | Должность: {emp['position']} | Кабинет: {emp['room_number']}")

def main():
    print("Программа «Фирма». Управление сотрудниками.")
    print("Доступные команды:")
    print("  add <ID> <ФИО> <телефон> <email> <должность> <кабинет> <skype> — добавить сотрудника")
    print("  remove <ID>                     — удалить сотрудника")
    print("  find <ID>                      — найти сотрудника")
    print("  update <ID> [поля]            — обновить данные (поля: name, phone, email, pos, room, skype)")
    print("  show                          — показать всех сотрудников")
    print("  exit                          — выйти\n")

    while True:
        command = input("\nВведите команду: ").strip()
        if not command:
            continue

        parts = command.split()
        action = parts[0].lower()

        if action == "exit":
            print("До свидания!")
            break

        elif action == "add" and len(parts) == 8:
            emp_id = parts[1]
            full_name = parts[2]
            phone = parts[3]
            email = parts[4]
            position = parts[5]
            room_number = parts[6]
            skype = parts[7]
            add_employee(emp_id, full_name, phone, email, position, room_number, skype)

        elif action == "remove" and len(parts) == 2:
            emp_id = parts[1]
            remove_employee(emp_id)

        elif action == "find" and len(parts) == 2:
            emp_id = parts[1]
            find_employee(emp_id)

        elif action == "show":
            show_all_employees()

        elif action == "update" and len(parts) >= 3:
            emp_id = parts[1]
            updates = {}
            for arg in parts[2:]:
                if arg.startswith("name="):
                    updates["full_name"] = arg[5:]
                elif arg.startswith("phone="):
                    updates["phone"] = arg[6:]
                elif arg.startswith("email="):
                    updates["email"] = arg[6:]
                elif arg.startswith("pos="):
                    updates["position"] = arg[4:]
                elif arg.startswith("room="):
                    updates["room_number"] = arg[5:]
                elif arg.startswith("skype="):
                    updates["skype"] = arg[6:]

            update_employee(emp_id, **updates)

        else:
            print("Неверная команда. Проверьте синтаксис и количество аргументов.")


main()
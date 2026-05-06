class Ticket:
    def __init__(self, ticket_id, employee_name, department, equipment_type,
                 inventory_number, problem_description, priority, status):
        self.id = ticket_id
        self.employee_name = employee_name
        self.department = department
        self.equipment_type = equipment_type
        self.inventory_number = inventory_number
        self.problem_description = problem_description
        self.priority = priority
        self.status = status

    def __str__(self):
        return (f"Номер заявки: {self.id}\n"
                f"Сотрудник: {self.employee_name}\n"
                f"Отдел: {self.department}\n"
                f"Оборудование: {self.equipment_type}\n"
                f"Инвентарный номер: {self.inventory_number}\n"
                f"Описание проблемы: {self.problem_description}\n"
                f"Приоритет: {self.priority}\n"
                f"Статус: {self.status}\n")


class ServiceDesk:
    def __init__(self, filename="tickets.txt"):
        self.tickets = []
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                ticket_data = {}

                for line in lines:
                    line = line.strip()
                    if not line:
                        continue

                    if line.startswith("Номер заявки: "):
                        if ticket_data:
                            self.add_ticket_from_dict(ticket_data)
                            ticket_data = {}
                        ticket_id = int(line.split(": ")[1])
                        ticket_data['id'] = ticket_id

                    elif line.startswith("Сотрудник: "):
                        ticket_data['employee_name'] = line.split(": ")[1]
                    elif line.startswith("Отдел: "):
                        ticket_data['department'] = line.split(": ")[1]
                    elif line.startswith("Оборудование: "):
                        ticket_data['equipment_type'] = line.split(": ")[1]
                    elif line.startswith("Инвентарный номер: "):
                        ticket_data['inventory_number'] = line.split(": ")[1]
                    elif line.startswith("Описание проблемы: "):
                        ticket_data['problem_description'] = line.split(": ")[1]
                    elif line.startswith("Приоритет: "):
                        ticket_data['priority'] = line.split(": ")[1]
                    elif line.startswith("Статус: "):
                        ticket_data['status'] = line.split(": ")[1]

            if ticket_data and 'status' in ticket_data:
                self.add_ticket_from_dict(ticket_data)

        except FileNotFoundError:
            print("Файл с данными не найден. Начинаем с пустого списка заявок.")

    def add_ticket_from_dict(self, ticket_data):
        ticket = Ticket(
            ticket_data['id'],
            ticket_data['employee_name'],
            ticket_data['department'],
            ticket_data['equipment_type'],
            ticket_data['inventory_number'],
            ticket_data['problem_description'],
            ticket_data['priority'],
            ticket_data['status']
        )
        self.tickets.append(ticket)

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for ticket in self.tickets:
                file.write(str(ticket) + "\n")
        print("Данные успешно сохранены.")

    def get_next_id(self):
        if not self.tickets:
            return 1
        return max(ticket.id for ticket in self.tickets) + 1

    def add_ticket(self):
        print("=== Добавление новой заявки ===")
        employee_name = input("ФИО сотрудника: ")
        department = input("Отдел сотрудника: ")
        equipment_type = input("Тип оборудования: ")
        inventory_number = input("Инвентарный номер оборудования: ")
        problem_description = input("Описание проблемы: ")

        while True:
            priority = input("Приоритет заявки (низкий/средний/высокий): ").lower()
            if priority in ['низкий', 'средний', 'высокий']:
                break
            print("Некорректный приоритет. Попробуйте снова.")

        status = "новая"
        ticket_id = self.get_next_id()

        ticket = Ticket(ticket_id, employee_name, department, equipment_type,
                     inventory_number, problem_description, priority, status)
        self.tickets.append(ticket)
        print(f"Заявка №{ticket_id} успешно добавлена!")

    def show_all_tickets(self):
        if not self.tickets:
            print("Заявки отсутствуют.")
            return

        for ticket in self.tickets:
            print(ticket)
            print("-" * 30)

    def search_tickets(self):
        print("=== Поиск заявок ===")
        print("1. Поиск по сотруднику")
        print("2. Поиск по отделу")
        print("3. Поиск по статусу")
        print("4. Поиск по инвентарному номеру")

        choice = input("Выберите критерий поиска (1-4): ")
        search_term = input("Введите значение для поиска: ").lower()
        found = False

        for ticket in self.tickets:
            if (choice == '1' and search_term in ticket.employee_name.lower() or
                choice == '2' and search_term in ticket.department.lower() or
                choice == '3' and search_term in ticket.status.lower() or
                choice == '4' and search_term in ticket.inventory_number.lower()):
                print(ticket)
                print("-" * 30)
                found = True

        if not found:
            print("Заявки не найдены.")

    def change_status(self):
        try:
            ticket_id = int(input("Введите номер заявки: "))
            ticket = next((t for t in self.tickets if t.id == ticket_id), None)

            if not ticket:
                print("Заявка с указанным номером не найдена.")
                return

            print("Выберите новый статус:")
            print("1. новая")
            print("2. в работе")
            print("3. выполнена")

            status_choice = input("Ваш выбор (1-3): ")
            new_status = {'1': 'новая', '2': 'в работе', '3': 'выполнена'}.get(status_choice)

            if new_status:
                ticket.status = new_status
                print("Статус заявки успешно изменён.")
            else:
                print("Некорректный выбор статуса.")
        except ValueError:
            print("Пожалуйста, введите корректный номер заявки.")

    def delete_ticket(self):
        try:
            ticket_id = int(input("Введите номер заявки для удаления: "))
            ticket = next((t for t in self.tickets if t.id == ticket_id), None)

            if ticket:
                self.tickets.remove(ticket)
                print("Заявка успешно удалена.")
            else:
                print("Заявка с указанным номером не найдена.")
        except ValueError:
            print("Пожалуйста, введите корректный номер заявки.")

    def show_statistics(self):
        total = len(self.tickets)
        new_count = sum(1 for t in self.tickets if t.status == 'новая')
        in_progress = sum(1 for t in self.tickets if t.status == 'в работе')
        completed = sum(1 for t in self.tickets if t.status == 'выполнена')
        high_priority = sum(1 for t in self.tickets if t.priority == 'высокий')

        print("=== Статистика ===")
        print(f"Всего заявок: {total}")
        print(f"Новые: {new_count}")
        print(f"В работе: {in_progress}")
        print(f"Выполнены: {completed}")
        print(f"С высоким приоритетом: {high_priority}")


    def main_menu(self):
        while True:
            print("\n=== ServiceDesk Console ===")
            print("1. Добавить заявку")
            print("2. Показать все заявки")
            print("3. Найти заявку")
            print("4. Изменить статус заявки")
            print("5. Удалить заявку")
            print("6. Показать статистику")
            print("7. Сохранить данные")
            print("0. Выход")

            choice = input("Выберите действие (0-7): ").strip()

            if choice == '1':
                self.add_ticket()
            elif choice == '2':
                self.show_all_tickets()
            elif choice == '3':
                self.search_tickets()
            elif choice == '4':
                self.change_status()
            elif choice == '5':
                self.delete_ticket()
            elif choice == '6':
                self.show_statistics()
            elif choice == '7':
                self.save_data()
            elif choice == '0':
                self.save_data()  # Автосохранение перед выходом
                print("Выход из программы. До свидания!")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")



def main():
    service_desk = ServiceDesk()
    service_desk.main_menu()

if __name__ == "__main__":
    main()
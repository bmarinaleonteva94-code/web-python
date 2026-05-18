from dataclasses import dataclass
from typing import Optional, List
import json

@dataclass
class Material:
    id: int
    name: str
    category: str
    unit: str
    quantity: int 
    min_quantity: int

@dataclass 
class Request:
    id: int
    employee_name: str
    department: str
    material_id: int
    quantity: int
    reason: str
    status: str


class WarehouseRequestRepository:
    def __init__(self, data_file: str = 'warehouse_data.json'):
        self.materials = []
        self.requests = []
        self.next_material_id = 1
        self.next_request_id = 1
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for m in data.get("materials", []):
                    self.materials.append(Material(**m))
                self.next_material_id = data.get("next_material_id", 1)
                for r in data.get("requests", []):
                    self.requests.append(Request(**r))
                self.next_request_id = data.get("next_request_id", 1)
            print("Данные успешно загружены.")
        except FileNotFoundError:
            print("Файл данных не найден. Начинаем с пустыми списками.")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Ошибка загрузки данных: {e}. Используются пустые списки.")

    def save_data(self):
        data = {
            "materials": [m.__dict__ for m in self.materials],
            "requests": [r.__dict__ for r in self.requests],
            "next_material_id": self.next_material_id,
            "next_request_id": self.next_request_id
        }
        try:
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("Данные успешно сохранены.")
        except Exception as e:
            print(f"Ошибка сохранения данных: {e}")
          
    def add_material(self, name: str, category: str, unit: str, quantity: int, min_quantity: int) -> Optional[Material]:
        if quantity < 0:
            print("Количество материала не может быть отрицательным.")
            return None
        if min_quantity < 0:
            print("Минимальный остаток не может быть отрицательным.")
            return None
        material = Material(
            id = self.next_material_id,
            name = name,
            category=category,
            unit=unit,
            quantity=quantity,
            min_quantity=min_quantity
        )
        self.materials.append(material)
        self.next_material_id += 1
        print("Материал успешно добавлен.")
        return material
    
    def get_all_materials(self):
        return self.materials
    
    def create_request(self, employee_name: str, department:str, material_id: int, quantity: int, reason: str, status: str) -> Optional[Request]: 
        material = self.find_material_by_id(material_id)
        if not material:
            print("Материал с указанным номером не найден.")
            return None
        if quantity <= 0:
            print("Количество в заявке должно быть больше нуля.")
            return None
        if quantity > material.quantity:
            print("Запрашиваемое количество превышает остаток на складе.")
            return None
        request = Request(
            id=self.next_request_id,
            employee_name=employee_name,
            department=department,
            material_id=material_id,
            quantity=quantity,
            reason=reason,
            status=status
        )
        self.requests.append(request)
        self.next_request_id += 1 
        print("Заявка успешно создана.")
        return request
    
    def get_all_requests(self) -> List[Request]:
        return self.requests
    
    def find_material_by_id(self, material_id: int) -> Optional[Material]:
        for material in self.materials:
            if material.id == material_id:
                return material
            return None
        
    def find_request_by_id(self, request_id: int) -> Optional[Request]:
        for request in self.requests:
            if request.id == request_id:
                return request
            return None
        
    def restock_material(self, material_id: int, add_quantity: int) -> bool:
        if add_quantity <= 0:
            print("Количество для пополнения должно быть больше нуля.")
            return False
        material = self.find_material_by_id(material_id)
        if material:
            material.quantity += add_quantity
            print("Остаток материала успешно пополнен.")
            return True
        else: 
            print("Материал с указанным номером не найден.")
            return False
    
    def update_request_status(self, request_id: int, new_status: str) -> bool:
        request = self.find_request_by_id(request_id)
        if request:
            request.status = new_status
            return True
        else:
            print("Заявка с указанным номером не найдена.")
            return False
    
    def write_off_material(self, request_id: int) -> bool:
        request = self.find_request_by_id(request_id)
        if not request:
            print ("Заявка с указанным номером не найдена.")
            return False
        if request.status != "одобрена":
            print("Списание возможно только по одобренной заявке.")
            return False
        material = self.find_material_by_id(request.material_id)
        if not material:
            print("Материал не найден.")
            return False
        if material.quantity < request.quantity:
            print("Недостаточно материала на складе.")
            return False
        material.quantity -= request.quantity
        request.status = 'выполнена'
        print('Материал успешно списан по заявке.')
        return True

    def search_requests(self, search_term: str, search_by: str) -> List[Request]:
        results = []
        search_term = search_term.lower()
        for request in self.requests:
            material = self.find_material_by_id(request.material_id)
            material_name = material.name.lower() if material else ""
            match = False
            if search_by == "employee" and search_term in request.employee_name.lower():
                match = True
            elif search_by == "department" and search_term in request.department.lower():
                match = True
            elif search_by == "material" and search_term in material_name:
                match = True
            elif search_by == "status" and search_term in request.status.lower():
                match = True
            if match:
                results.append(request)
        return results

    def get_statistics(self) -> dict:
        low_stock_count = sum(1 for m in self.materials if m.quantity <= m.min_quantity)
        total_units = sum(m.quantity for m in self.materials)
        status_counts = {'новая': 0, 'одобрена': 0, 'отклонена': 0, 'выполнена': 0}
        for req in self.requests:
            if req.status in status_counts:
                status_counts[req.status] += 1
        return {
            'total_materials': len(self.materials),
            'total_requests': len(self.requests),
            **status_counts,
            'low_stock_count': low_stock_count,
            'total_units': total_units
        }


class WarehouseRequestConsole:
    def __init__(self):
        self.repository = WarehouseRequestRepository

    def show_menu(self):
        print("\n === WarehouseRequest Console ===\n ")
        print(" 1. Добавить материал на склад")
        print(" 2. Показать все материалы")
        print(" 3. Создать заявку на выдачу")
        print(" 4. Показать все заявки")
        print(" 5. Найти заявку")
        print(" 6. Изменить статус заявки")
        print(" 7. Пополнить остаток материала")
        print(" 8. Списать материал по заявке")
        print(" 9. Показать статистику")
        print(" 10. сохранить данные")
        print(" 0. Выход")        
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Выберите пункт меню: ").strip()
            if choice == "1":
                self.add_material()
            elif choice == "2":
                self.show_all_materials()
            elif choice == "3":
                self.create_request()
            elif choice == "4":
                self.show_all_requests()
            elif choice == "5":
                self.search_requests()
            elif choice == "6":
                self.update_request_status()
            elif choice == "7":
                self.restock_material()
            elif choice == "8":
                self.write_off_material()
            elif choice == "9":
                self.show_statistics()
            elif choice == "10":
                self.save_data()
            elif choice == "0":
                self.save_data()
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")

    def add_material(self):
        name = input("Название материала: ")
        category = input("Категория материала: ")
        unit = input("Единица измерения: ")
        try:
            quantity = int(input("Количество на складе: "))
            min_quantity = int(input("Минимальный остаток: "))
        except ValueError:
            print("Ошибка: количество и минимальный остаток должны быть целыми числами.")
            return
        self.repository.add_material(name, category, unit, quantity, min_quantity)

    def show_all_materials(self):
        materials = self.repository.get_all_materials()
        if not materials:
            print("Материалы отсутствуют.")
            return
        print("\n=== Список материалов ===")
        for material in materials:
            status = "Требуется пополнение" if material.quantity <= material.min_quantity else "В наличии"
            print(f"Номер материала: {material.id}")
            print(f"Название: {material.name}")
            print(f"Категория: {material.category}")
            print(f"Единица измерения: {material.unit}")
            print(f"Количество на складе: {material.quantity}")
            print(f"Минимальный остаток: {material.min_quantity}")
            print(f"Статус остатка: {status}")
            print("-" * 30)

    def create_request(self):
        employee_name = input("ФИО сотрудника: ")
        department = input("Отдел: ")
        try:
            material_id = int(input("Номер материала: "))
            quantity = int(input("Количество материала: "))
        except ValueError:
            print("Ошибка: номер материала и количество должны быть целыми числами.")
            return
        reason = input("Причина выдачи: ")
        status = input("Статус заявки (новая/одобрена/отклонена/выполнена): ")
        valid_statuses = ["новая", "одобрена", "отклонена", "выполнена"]
        if status not in valid_statuses:
            print("Недопустимый статус заявки. Допустимые значения: новая, одобрена, отклонена, выполнена.")
            return
        self.repository.create_request(employee_name, department, material_id, quantity, reason, status)

    def show_all_requests(self):
        requests = self.repository.get_all_requests()
        if not requests:
            print("Заявки отсутствуют.")
            return

        print("\n=== Список заявок ===")
        for request in requests:
            material = self.repository.find_material_by_id(request.material_id)
            material_name = material.name if material else "Неизвестный материал"
            print(f"Номер заявки: {request.id}")
            print(f"Сотрудник: {request.employee_name}")
            print(f"Отдел: {request.department}")
            print(f"Материал: {material_name}")
            print(f"Количество: {request.quantity} {material.unit if material else ''}")
            print(f"Причина выдачи: {request.reason}")
            print(f"Статус: {request.status}")
            print("-" * 40)

    def search_requests(self):
        print("\n1. Поиск по сотруднику")
        print("2. Поиск по отделу")
        print("3. Поиск по материалу")
        print("4. Поиск по статусу")
        search_choice = input("Выберите критерий поиска: ").strip()
        search_by_map = {
            "1": "employee",
            "2": "department",
            "3": "material",
            "4": "status"
        }
        if search_choice not in search_by_map:
            print("Некорректный выбор критерия поиска.")
            return
        search_term = input("Введите поисковый запрос: ")
        results = self.repository.search_requests(search_term, search_by_map[search_choice])
        if not results:
            print("Заявки не найдены.")
            return
        print("\n=== Результаты поиска ===")
        for request in results:
            material = self.repository.find_material_by_id(request.material_id)
            material_name = material.name if material else "Неизвестный материал"
            print(f"№{request.id}: {request.employee_name}, {material_name} — {request.status}")

    def update_request_status(self):
        try:
            request_id = int(input("Введите номер заявки: "))
        except ValueError:
            print("Ошибка: номер заявки должен быть целым числом.")
            return
        print("Выберите новый статус:")
        print("1. новая")
        print("2. одобрена")
        print("3. отклонена")
        print("4. выполнена")
        status_choice = input("Ваш выбор: ").strip()
        status_map = {"1": "новая", "2": "одобрена", "3": "отклонена", "4": "выполнена"}
        new_status = status_map.get(status_choice)
        if not new_status:
            print("Некорректный выбор статуса.")
            return
        self.repository.update_request_status(request_id, new_status)

    def restock_material(self):
        try:
            material_id = int(input("Введите номер материала: "))
            add_quantity = int(input("Введите количество для пополнения: "))
        except ValueError:
            print("Ошибка: номер материала и количество должны быть целыми числами.")
            return
        self.repository.restock_material(material_id, add_quantity)

    def write_off_material(self):
        try:
            request_id = int(input("Введите номер заявки для списания: "))
        except ValueError:
            print("Ошибка: номер заявки должен быть целым числом.")
            return
        self.repository.write_off_material(request_id)

    def show_statistics(self):
        stats = self.repository.get_statistics()
        print("\n=== Статистика ===")
        print(f"Всего материалов: {stats['total_materials']}")
        print(f"Всего заявок: {stats['total_requests']}")
        print(f"Новые заявки: {stats['новая']}")
        print(f"Одобренные заявки: {stats['одобрена']}")
        print(f"Отклоненные заявки: {stats['отклонена']}")
        print(f"Выполненные заявки: {stats['выполнена']}")
        print(f"Материалы, требующие пополнения: {stats['low_stock_count']}")
        print(f"Всего единиц материалов на складе: {stats['total_units']}")

    def save_data(self):
        self.repository.save_data()

if __name__ == "__main__":
    console = WarehouseRequestConsole()
    console.run()
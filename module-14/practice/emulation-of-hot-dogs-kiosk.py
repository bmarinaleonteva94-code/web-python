from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from datetime import datetime
import json
import os

TOPPING_MAYO = "Майонез"
TOPPING_MUSTARD = "Горчица"
TOPPING_KETCHUP = "Кетчуп"
TOPPING_SWEET_ONION = "Сладкий лук"
TOPPING_JALAPENO = "Халапеньо"
TOPPING_CHILI = "Чили"
TOPPING_PICKLE = "Солёный огурец"

ALL_TOPPINGS = [
    TOPPING_MAYO,
    TOPPING_MUSTARD,
    TOPPING_KETCHUP,
    TOPPING_SWEET_ONION,
    TOPPING_JALAPENO,
    TOPPING_CHILI,
    TOPPING_PICKLE
]

@dataclass
class HotDogRecipe:
    name: str
    base_price: float
    default_toppings: List[str] = field(default_factory=list)

@dataclass
class InventoryItem:
    name: str
    quantity: int
    threshold: int=10

    def use(self, amount:int) -> bool:
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False
    
    @property 
    def is_low(self) -> bool:
        return self.quantity <= self.threshold

@dataclass
class HotDog:
    recipe: HotDogRecipe
    custom_toppings: List[str] = field(default_factory=list)
    quantity: int = 1

    @property
    def toppings(self) -> List[str]:
        return list(set(self.recipe.default_toppings + self.custom_toppings))
    
    @property
    def price(self) -> float:
        base_price = self.recipe.base_price
        topping_price = len(self.toppings) * 0.5
        total_price = base_price + topping_price

        if self.quantity >= 3:
            discount = 0.05 * (self.quantity // 3)
            total_price *= (1-discount)
        return round(total_price * self.quantity, 2)

    def __str__(self) -> str:
        toppings_str = ", ".join(self.toppings) if self.toppings else 'без топпингов'
        return f'{self.recipe.name} - {self.quantity} шт.; топпинги: {toppings_str} - {self.price} руб.'

@dataclass
class Order:
    hotdogs: List[HotDog] = field(default_factory=list)
    payment_method: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)

    @property
    def total_amount(self) -> float:
        return sum(hd.price for hd in self.hotdogs)

    def add_hotdog(self, hotdog: HotDog) -> None:
        self.hotdogs.append(hotdog)

    def save_to_file(self) -> None:
        order_data = {
            "timestamp": self.timestamp.isoformat(),
            "hotdogs": [
                {
                    "recipe_name": hd.recipe.name,
                    "quantity": hd.quantity,
                    "toppings": hd.toppings,
                    "price": hd.price
                } for hd in self.hotdogs
            ],
            "total_amount": self.total_amount,
            "payment_method": self.payment_method
        }

        filename = f"order_{self.timestamp.strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(order_data, f, ensure_ascii=False, indent=2)
        print(f"Заказ сохранён в файл: {filename}")

class InventoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.items = {}
            cls._instance.observers = []
        return cls._instance

    def add_item(self, name: str, quantity: int, threshold: int = 10):
        self.items[name] = InventoryItem(name, quantity, threshold)

    def get_item(self, name: str) -> Optional[InventoryItem]:
        return self.items.get(name)

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_low_stock(self, item: InventoryItem):
        for observer in self.observers:
            observer.on_low_stock(item)

    def check_stock(self) -> List[InventoryItem]:
        low_items = []
        for item in self.items.values():
            if item.is_low:
                low_items.append(item)
                self.notify_low_stock(item)
        return low_items

class StatisticsManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.total_hotdogs = 0
            cls._instance.revenue = 0.0
            cls._instance.profit = 0.0
        return cls._instance

    def record_sale(self, quantity: int, total_amount: float, cost: float = 0):
        self.total_hotdogs += quantity
        self.revenue += total_amount
        self.profit += (total_amount - cost)

    def get_statistics(self) -> Dict:
        return {
            "total_hotdogs": self.total_hotdogs,
            "revenue": self.revenue,
            "profit": self.profit
        }

class SalesReport:
    @staticmethod
    def generate_report():
        stats = StatisticsManager().get_statistics()
        print("\n=== ОТЧЁТ О ПРОДАЖАХ ===")
        print(f"Всего продано хот‑догов: {stats['total_hotdogs']}")
        print(f"Выручка: {stats['revenue']} руб.")
        print(f"Прибыль: {stats['profit']} руб.")

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f'Оплата наличными на сумму: {amount} руб.')
        return True

class CardPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f'Оплата картой на сумму: {amount} руб.')
        return True

class HotDogKiosk:
    def __init__(self):
        self.inventory = InventoryManager()
        self.statistics = StatisticsManager()
        self.recipes = self._load_recipes()
        self._initialize_inventory()

    def _load_recipes(self) -> List[HotDogRecipe]:
        return [
            HotDogRecipe("Классический", 3.0, [TOPPING_KETCHUP, TOPPING_MUSTARD]),
            HotDogRecipe("Острый", 3.5, [TOPPING_JALAPENO, TOPPING_CHILI]),
            HotDogRecipe("Гурман", 4.0, [TOPPING_MAYO, TOPPING_SWEET_ONION, TOPPING_PICKLE])
        ]

    def _initialize_inventory(self):
        ingredients = [
            ("Булочки", 50),
            ("Сосиски", 50),
            ("Майонез", 30),
            ("Горчица", 30),
            ("Кетчуп", 30),
            ("Сладкий лук", 20),
            ("Халапеньо", 20),
            ("Чили", 20),
            ("Солёные огурцы", 20)
        ]
        for name, quantity in ingredients:
            self.inventory.add_item(name, quantity)

    def display_menu(self):
        print("\n=== МЕНЮ КИОСКА ===")
        for i, recipe in enumerate(self.recipes, 1):
            toppings_str = ", ".join(recipe.default_toppings) if recipe.default_toppings else "без топпингов"
            print(f"{i}. {recipe.name} — {recipe.base_price} руб. (по умолчанию: {toppings_str})")
        print("4. Создать свой рецепт")

    def select_recipe(self) -> HotDogRecipe:
        while True:
            try:
                choice = int(input("Выберите рецепт (1-4): "))
                if 1 <= choice <= 3:
                    return self.recipes[choice - 1]
                elif choice == 4:
                    return self._create_custom_recipe()
                else:
                    print("Неверный выбор. Попробуйте снова.")
            except ValueError:
                print("Пожалуйста, введите число.")

    def _create_custom_recipe(self) -> HotDogRecipe:
        name = input("Введите название вашего рецепта: ")
        while True:
            try:
                price = float(input("Введите цену: "))
                break
            except ValueError:
                print("Цена должна быть числом. Попробуйте снова.")

        print("Доступные топпинги:")
        for i, topping in enumerate(ALL_TOPPINGS, 1):
            print(f"{i}. {topping}")

        selected_toppings = []
        while True:
            try:
                topping_choice = input("Выберите топпинг (введите номер, 0 для завершения): ")
                if topping_choice == "0":
                    break
                topping_idx = int(topping_choice) - 1
                if 0 <= topping_idx < len(ALL_TOPPINGS):
                    selected_toppings.append(ALL_TOPPINGS[topping_idx])
                    print(f"Добавлен: {ALL_TOPPINGS[topping_idx]}")
                else:
                    print("Неверный номер топпинга.")
            except ValueError:
                print("Пожалуйста, введите номер топпинга или 0 для завершения.")

        return HotDogRecipe(name, price, selected_toppings)

    def select_toppings(self, current_toppings: List[str]) -> List[str]:
        selected = set(current_toppings)
        print("\nДоступные для добавления топпинги:")
        for i, topping in enumerate(ALL_TOPPINGS, 1):
            status = "✓" if topping in selected else " "
            print(f"{i}. [{status}] {topping}")

        while True:
            try:
                choice = input("Выберите топпинг для добавления (0 для завершения): ")
                if choice == "0":
                    break
                topping_idx = int(choice) - 1
                if 0 <= topping_idx < len(ALL_TOPPINGS):
                    selected.add(ALL_TOPPINGS[topping_idx])
                else:
                    print("Неверный номер.")
            except ValueError:
                print("Введите число или 0 для завершения.")
        return list(selected)

    def process_order(self) -> Order:
        order = Order()

        while True:
            recipe = self.select_recipe()
            additional_toppings = self.select_toppings(recipe.default_toppings)
    
            while True:
                try:
                    quantity = int(input("Укажите количество хот‑догов: "))
                    if quantity > 0:
                        break
                except ValueError:
                    print("Количество должно быть положительным числом.")

            hotdog = HotDog(recipe, additional_toppings, quantity)
            order.add_hotdog(hotdog)

            if input("Добавить ещё хот‑дог? (да/нет): ").lower() != "да":
                break

        print("\nВаш заказ:")
        for hd in order.hotdogs:
            print(f"- {hd}")
        print(f"Общая сумма: {order.total_amount} руб.")

        payment_choice = input("Способ оплаты (1 — наличные, 2 — карта): ")
        if payment_choice == "1":
            payment = CashPayment()
            order.payment_method = "Наличные"
        else:
            payment = CardPayment()
            order.payment_method = "Карта"

        if payment.pay(order.total_amount):
            order.save_to_file()
            total_quantity = sum(hd.quantity for hd in order.hotdogs)
            self.statistics.record_sale(total_quantity, order.total_amount)
            low_items = self.inventory.check_stock()
            if low_items:
                print("\nВНИМАНИЕ: Требуется пополнение запасов:")
                for item in low_items:
                    print(f"- {item.name}: осталось {item.quantity} шт.")
        return order

    def show_statistics(self):
        SalesReport.generate_report()

    def check_inventory(self):
        print("\n=== СОСТОЯНИЕ ЗАПАСОВ ===")
        low_items = []
        for item_name, item in self.inventory.items.items():
            status = "НИЗКИЙ" if item.is_low else "НОРМА"
            print(f"{item_name}: {item.quantity} шт. ({status})")
            if item.is_low:
                low_items.append(item)

        if low_items:
            print("\nТРЕБУЕТСЯ ПОПОЛНЕНИЕ:")
            for item in low_items:
                print(f"- {item.name}: осталось {item.quantity} шт., порог: {item.threshold}")

    def on_low_stock(self, item: InventoryItem):
        print(f"ВНИМАНИЕ: Низкий запас {item.name}! Осталось: {item.quantity} шт. (порог: {item.threshold})")

    def run(self):
        print("Добро пожаловать в киоск по продаже хот‑догов!")
        while True:
            print("\n=== ГЛАВНОЕ МЕНЮ ===")
            print("1. Сделать заказ")
            print("2. Посмотреть статистику продаж")
            print("3. Проверить запасы ингредиентов")
            print("4. Выйти")
            choice = input("Выберите действие (1-4): ")
            if choice == "1":
                self.process_order()
            elif choice == "2":
                self.show_statistics()
            elif choice == "3":
                self.check_inventory()
            elif choice == "4":
                print("Спасибо за работу! До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

def main():
    kiosk = HotDogKiosk()
    kiosk.run()

if __name__ == "__main__":
    main()


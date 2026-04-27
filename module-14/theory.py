#  S - Single Responsibility

class BadReport:             # плохой пример решения задачи
    def __init__(self, title, rows):
        self.title = title
        self.rows = rows

    def as_text(self):
        lines = [self.title, "-" * len(self.rows)]
        for row in self.rows:
            lines.append(f"{row["name"]}: {row["value"]}")
        return "\n".join(lines) 
    
    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.as_text())

        

# правильный вариант решения задачи.      Разные классы дя разных задач: форматирование текста и сохранение
from dataclasses import dataclass

@dataclass
class Report:
    title: str
    rows: list[dict]

class TextReportFormatter:
    def format(self, report: Report) -> str:
        lines = [report.title, "-" * len(report.rows)]
        for row in report.rows:
            lines.append(f"{row["name"]}: {row["value"]}")
        return "\n".join(lines)
    
class FileStorage:
    def save(self, filename: str, content: str) -> None:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

report = Report("Продажи", [{"name": "Книги", "value": 100}])
print(TextReportFormatter().format(report))



# O - Open/Closed

# Плохой пример
def calculate_discount_bad(customer_type: str, amount: float) -> float:
    if customer_type == 'regular':
        return amount * 0.05
    if customer_type == 'vip':
        return amount * 0.15
    if customer_type == 'customer':
        return amount * 0.30
    return 0
print(calculate_discount_bad("regular", 1000))

#  Правильный вариант
from typing import Protocol

class Discount(Protocol):
    def discount_for(self, amount: float) -> float:
        ...

class RegularDiscount:
    def discount_for(self, amount: float) -> float:
        return amount * 0.05
    
class VipDiscount:
    def discount_for(self, amount: float) -> float:
        return amount * 0.15

class CustomerDiscount:
    def discount_for(self, amount: float) -> float:
        return amount * 0.30
    
class NoDiscount:
    def discount_for(self, amount: float) -> float:
        return 0
    
def final_price(amount: float, discount: Discount) -> float:
    return amount - discount.discount_for(amount)



#  L - Liskov Substitution

#  Плохой пример
class BadBird:
    def fly(self):
        print("Летит")

class BadSparrow(BadBird):
    pass

class BadPinquin(BadBird):
    def fly(self):
        raise ValueError("Пингвины не летают")
    
def make_bird_fly(bird: BadBird):
    bird.fly()

make_bird_fly(BadSparrow())
try: 
    make_bird_fly(BadPinquin())
except ValueError as e:
    print("Ошибка: ", e)


#  Хороший пример
from dataclasses import dataclass
from typing import Protocol

@dataclass
class Bird:
    name: str

class Flyable(Protocol):
    def fly(self) -> None:
        ...

class Sparrow(Bird):
    def fly(self):
        print(f"{self.name} летит")

class Pinquin(Bird):
    def swim(self):
        print(f"{self.name} плывет")

def make_fly(obj: Flyable):
    obj.fly()

make_fly(Sparrow("Воробей"))
Pinquin("Пингвин").swim()




#  I - Interface Segregation (Принцип разделения интерфейса)

#  Плохой пример
from abc import ABC, abstractmethod
class BadDeviceOffice(ABC):
    @abstractmethod
    def print_document(self, text: str) -> None:
        pass

    @abstractmethod
    def scan_document(self) -> None:
        pass

    @abstractmethod
    def send_fax(self, phone: str, text: str) -> None:
        pass

class Printer(BadDeviceOffice):
    def print_document(self, text: str) -> None:
        print("Печать: ", text)

    def scan_document(self) -> None:
        raise NotImplementedError("Принтер не сканирует")
    
    def send_fax(self, phone: str, text: str) -> None:
        raise NotImplementedError("принтер не отправляет факс")
    
    #  Хороший пример
from typing import Protocol
class Printer(Protocol):
    def print_document(self, text: str) -> None:
        ...

class Scanner(Protocol):
    def scan_document(self, text: str) -> None:
        ...
class LPrinter:
    def print_document(self, text: str) -> None:
        print("Печать документа")
class MFPrinter:
    def print_document(self, text: str) -> None:
        print("Печать документа")

    def scan_document(self) -> str:
        return "Скан готов"
      
def print_document(device: Printer):
    device.print_document("Документ")

def scan_document(device: Scanner):
    device.scan_document()

print_document(LPrinter())
print_document(MFPrinter())
print(scan_document(MFPrinter()))



#  D - Dependency Inversion (принцип инверсии зависимостей)

# плохой пример
class EmailSender:
    def send(self, email: str, message: str) -> None:
        print(f"Email для {email}: {message}")

class BadOrderService:
    def __init__(self):
        self.sender = EmailSender()

    def complete_order(self, email: str, total: float) -> None:
        print(f"Заказ на сумму {total} оформлен")
        self.sender.send(email, "Ваш заказ оформлен")

BadOrderService().complete_order("user@example.com", 3500)



# хороший пример
from typing import Protocol

class Notifier(Protocol):
    def send(self, contact: str, message: str) -> None:
        ...

class EmailNotifier:
    def send(self, contact: str, message: str) -> None:
        print(f"Email для {contact}: {message}")

class SMSNotifier:
    def send(self, contact: str, message: str) -> None:
        print(f"SMS для {contact}: {message}")

class OrderService:
    def __init__(self, notifier: Notifier):
        self.sender = notifier

    def complete_order(self, email: str, total: float) -> None:
        print(f"Заказ на сумму {total} оформлен")
        self.sender.send(email, "Ваш заказ оформлен")

OrderService(EmailNotifier()).complete_order("user@example.com", 3500)
OrderService(SMSNotifier()).complete_order("+79000000000", 2000)
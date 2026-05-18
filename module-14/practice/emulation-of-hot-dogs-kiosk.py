from abc import ABC, abstractmethod
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    quantity: int
    threshold: int

 
class HotDogRecipe(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

class StandartHotDog:
    pass

class CustomHotDog:
    pass

class SalesReport:
    pass

class Order:
    pass



class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f'Оплата наличными на сумму: {amount} руб.'

class CardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f'Оплата картой на сумму: {amount} руб.'




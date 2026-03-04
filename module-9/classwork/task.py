lines = [
    "P-1;Mouse;25;Periphery",
    "P-2;Keyboard;45;Periphery",
    "P-3;Cloud VM;120;Services",
    "P-2;Duplicate;50;Periphery",
    "P-4;Broken;-5;Services",
    "P-5;BadPrice;abc;Services",
]


def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False
    # TODO: вернуть True, если text можно считать числом (включая дроби и знак), иначе False


class Product:
    def __init_(self, id, name, price, category):
        self.id = id
        self.name = name
        self._price = price
        self.category = category
    # TODO: __init__(id, name, price, category)

    @property
    def price(self):
        return self._price
    # TODO: property price (только getter)

    def set_price(self, value):
        if is_number(value) and float(value) >= 0:
            self._price = float(value)
            return True
        return False
    # TODO: set_price(value) -> bool

    @classmethod
    def from_line(cls, raw):
        parts = raw.split(";")
        if len(parts) != 4:
            return None, "Invalid line format"

        product_id, name, price_str, category = parts

        if not is_number(price_str):
            return None, f"Price '{price_str}' is not a valid number"

        price = float(price_str)
        if price < 0:
            return None, f"Price {price} is negative"

        return cls(product_id, name, price, category), None
    # TODO: classmethod from_line(cls, raw) -> (product_or_none, reason)

class ProductRegistry:
    def __init__(self):
        self.products = []
        self.ids = set()
    # TODO: __init__ (products list + id set)

    def add(self, product):
        self.products.append(product)
    # TODO: add(product) -> (bool, reason)


    # TODO: count()


    # TODO: all_products()


    # TODO: has_id(id)


    # TODO: by_category()


    # TODO: avg_price()



# TODO: создать registry и problems
# TODO: пройти по lines, загрузить валидные товары
# TODO: проблемные строки добавлять в problems как (line, reason)
# TODO: вывести count, by_category, avg_price и problems

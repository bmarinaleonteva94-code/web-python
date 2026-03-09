# class Employee:
#     pass
# e = Employee()
# print(type(e))   #  покажет тип переменной, функции и т.д.

from abc import ABC, abstractmethod

class Employee_base(ABC):
    def __init__ (self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def compensation(self):
        pass

class Employee(Employee_base):
    company = "1234"

    def __init__(self, emp_id, name, salary):     # 
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self._salary = 0

    def __str__(self):
        return f"{self.name}: {self.salary}"
    
    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.emp_id == other.emp_id

    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.salary < other.salary

    def compensation(self):
        return self.salary * 12
    
    # def info(self):
    #     return f"{self.name} -> {self.salary}"
    
    # @classmethod
    # def from_string(cls, raw):
    #     emp_id, name, salary = raw.split(",")
    #     return cls(int(emp_id), name, int(salary))
    
    # @staticmethod
    # def valid_name(name):
    #     return len(name.strip()) >= 2
    
    # def get_salary(self):
    #     return self.salary
    
    # def set_salary(self, value):
    #     if value < 0:
    #         self.salary = 0
    #     else:
    #         self.salary = value

    # @property
    # def salary(self):
    #     return self._salary
    
    # @salary.setter
    # def salary (self, value):
    #     self._salary = value

    # @salary.deleter
    # def salary(self):
    #     self._salary = 0

    def yearly_income(self):
        return self.salary * 12
    
class LoggableMixin:
    def log(self, message):
        print(f"[LOG] {self.name}: {message}")

class Manager(Employee, LoggableMixin):
    def __init__(self, emp_id, name, salary, bonus):
        super().__init__(emp_id, name, salary)
        self.bonus =  bonus

    def yearly_income(self):
        return super().yearly_income() + self.bonus

e = Manager(3, "Alex", 2000, 5000)
m = Manager(3, "Alice", 2000, 200)
m1 = Manager(4, "Alex", 3000, 200)
print(m == m1)
print(m > m1)
# print(e.log("12342233"))
# print(e.yearly_income())


# e = Employee.from_string("2, Andrew, 1000")

# e.salary = 5000
# print(e.salary)

# del e.salary
# print(e.salary)

# e.set_salary(4000)
# print(e.get_salary(), e.salary)

# print(e.emp_id, e.name, e.salary, Employee.valid_name(e.name))
# e = Employee(1, "Alice", 1000)
# print(e.name, e.salary, Employee.company)
# print(e.info())

# print(Manager.__mro__)     # покажет порядок насследования
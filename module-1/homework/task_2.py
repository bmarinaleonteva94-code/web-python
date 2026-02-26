salary = float(input("Введите зарплату за месяц: "))
loan_payment = float(input("Платеж по кредиту: "))
utilities_payment = float(input("Платеж за коммунальные услуги: "))
balance = salary - loan_payment - utilities_payment
print(balance)
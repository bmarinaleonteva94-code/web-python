prices = {
    "bread": 50,
    "milk": 80,
    "cheese": 200
}
cart = {
    "bread": 2,
    "cola": 1,
    "milk": 3,
    "cheese": 2
}
cart_cost = 0 
for item, count in cart.items():
    if item in prices:
        cart_cost +=prices[item] * count    #cart_cost += prices.get(key) * value
    else:
        print(f"Товар {item} не найден, его стоимость не учитывается!")
print(f"Стоимость корзины: {cart_cost}")
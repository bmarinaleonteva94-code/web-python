def happy_number(num):
    numbers = [int(d) for d in str(num)]
    if len(numbers) != 6:
        print("Число не шестизначное!")
        return
    first_sum = sum(numbers[:3])
    second_sum = sum(numbers[3:])
    if first_sum == second_sum:
        print(f"Число {num} счастливое")
    else: 
        print(f"Число {num} не счастливое")

happy_number(1234)
happy_number(123123)
happy_number(123456)
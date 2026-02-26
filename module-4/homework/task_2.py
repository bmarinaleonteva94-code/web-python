#            Быки-коровы

# # number1 = [random.randint(1,9) for _ in range(1)]
# # number2 = [random.randint(0,9) for _ in range(3)]
# # generate_number = number1 + number2
# # secret_num = ''.join(map(str,generate_number))
# # print(secret_num)

import random

def generate_secret():
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] == 0:
        for i in range(1, 4):
            if digits[i] != 0:
                digits[0], digits[i] = digits[i], digits[0]
                break
    return ''.join(map(str, digits[:4]))


def count_cows_bulls(secret, guess):
    cows = 0
    bulls = 0
    remaining_secret = {}
    remaining_guess = {}
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        else:
            remaining_secret.setdefault(secret[i], 0)
            remaining_secret[secret[i]] += 1
            
            remaining_guess.setdefault(guess[i], 0)
            remaining_guess[guess[i]] += 1
    for key in remaining_guess.keys():
        if key in remaining_secret:
            bulls += min(remaining_guess[key], remaining_secret[key])

    return cows, bulls

def validate_input(user_input):
    if not user_input.isdigit():
        return False, "Введите только цифры."
    if len(user_input) != 4:
        return False, "Число должно быть четырёхзначным."
    if user_input[0] == '0':
        return False, "Число не может начинаться с 0."
    if len(set(user_input)) != 4:
        return False, "Цифры не должны повторяться."
    return True, ""

def game_loop():
    secret = generate_secret()
    attempts = 0
    while True:
        guess = input("Введите ваше предположение: ").strip()
        is_valid, message = validate_input(guess)
        if not is_valid:
            print(f"!Ошибка: {message}")
            continue
        
        attempts += 1
        cows, bulls = count_cows_bulls(secret, guess)
        print(f"Коровы: {cows}, Быки: {bulls}")
        
        if cows == 4:
            print(f"Поздравляю! Вы угадали число {secret} за {attempts} попыток.")
            break
game_loop()
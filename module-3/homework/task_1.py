str = input("Введите любую строку: ")
cleaned_str = "".join(char.lower() for char in str if char.isalnum())
reverse_str = cleaned_str[::-1]
if reverse_str == cleaned_str:
    print(f'Строка "{str}" является палиндромом')
else:
    print(f'Строка "{str}" не является палиндромом')
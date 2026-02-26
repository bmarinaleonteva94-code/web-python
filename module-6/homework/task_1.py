basketball_players = []

def add_players():
    while True:
        name = input("Введите имя баскетболиста: ")
        if not name:
            print("Имя не может быть пустым!")
            continue
        try:
            height = float(input("Введите рост баскетболиста (см): "))
            if height <= 0:
                print("Рост должен быть положительным числом!")
                continue
        except ValueError:
            print("Ошибка: введите число для роста!")
            continue
        if any(player["name"] == name for player in basketball_players):
            print(f"Игрок '{name}' уже есть в списке!")
            continue

        new_player = {"name": name, "height": height}
        basketball_players.append(new_player)
        print(f"Баскетболист '{name}' добавлен.")

        add_more = input("Хотите добавить следующего баскетболиста? (yes/no)): ").lower()
        if add_more not in ("да", "yes", "y"):
            break
    show_players()

def delete_player():
    if not basketball_players:
        print("Список игроков пуст!")
        return
    name_to_remove = input("Кого необходимо удалить? ")
    if not name_to_remove:
        print("Имя не может быть пустым!")
        return
    for i, player in enumerate(basketball_players):
        if player["name"] == name_to_remove:
            del basketball_players[i]
            print(f"Игрок '{name_to_remove}' удалён.")
            return
    print(f"Игрока '{name_to_remove}' нет в списке!")

def show_players():
    if not basketball_players:
        print("Список игроков пуст.")
        return

    print("Текущий список игроков:")
    for i, player in enumerate(basketball_players, 1):
        print(f"{i}. {player['name']} — {player['height']} см")
    print()

def find_player(name):
    for player in basketball_players:
        if player["name"] == name:
            print(f"Найден: {player['name']} — рост {player["height"]} см.")
            return True
        print(f"Игрок '{name}' не найден в базе.")
        return False

def update_player(name, new_height):
    for player in basketball_players:
        if player["name"] == name:
            if not isinstance(new_height, (int, float)) or new_height <=0:
                print("Ошибка: рост должен быть положительным числом!")
                return False
            player["height"] = new_height
            print(f"Рост игрока '{name}' обновлён до {new_height} см.")
            return True
    print(f"Ошибка: игрок '{name}' не найден в базе!")
    return False

def main():
    while True:
        print("Доступные команды:")
        print("1. Добавить игроков (add)")
        print("2. Удалить игрока (delete)")
        print("3. Поиск игрока (find)")
        print("4. Изменение данных игрока (update)")
        print("5. Показать всех (show)")
        print("6. Выход (exit)")

        command = input("Введите команду (add/delete/show/exit): ").strip().lower()

        if command == "add":
            add_players()
        elif command == "delete":
            delete_player()
        elif command == "find":
            name = input("ФИО баскетболиста для поиска: ").strip()
            find_player(name)
        elif command == "update":
            name = input("ФИО баскетболиста для обновления: ").strip()
            try:
                new_height = float(input("Новый рост (см): "))
            except ValueError:
                print("Ошибка: введите число для роста!")
                continue
            update_player(name, new_height)
        elif command == "show":
            show_players()
        elif command == "exit":
            print("Программа завершена.")
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")

main()
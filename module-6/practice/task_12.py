#  Англо-французский словарь

dictionary = {}


def add_word(english, french):
    if english in dictionary:
        print(f"Слово '{english}' уже есть в словаре. Перевод: {dictionary[english]}")
    else:
        dictionary[english] = french
        print(f"Слово '{english}' добавлено с переводом '{french}'.")

def remove_word(english):
    if english in dictionary:
        del dictionary[english]
        print(f"Слово '{english}' удалено из словаря.")
    else:
        print(f"Слово '{english}' не найдено в словаре.")

def find_word(english):
    if english in dictionary:
        print(f"Перевод слова '{english}': '{dictionary[english]}'")
    else:
        print(f"Слово '{english}' не найдено в словаре.")

def replace_word(english, new_french):
    if english in dictionary:
        dictionary[english] = new_french
        print(f"Перевод слова '{english}' обновлён на '{new_french}'.")
    else:
        print(f"Слово '{english}' не найдено в словаре. Используйте add_word для добавления.")

def show_all():
    if dictionary:
        print("\nТекущий словарь:")
        for eng, fr in dictionary.items():
            print(f"{eng} → {fr}")
    else:
        print("Словарь пуст.")

def main():
    print("Англо-французский словарь. Доступные команды:")
    print("  add <слово> <перевод>     — добавить слово")
    print("  remove <слово>          — удалить слово")
    print("  find <слово>            — найти перевод")
    print("  replace <слово> <новый> — заменить перевод")
    print("  show                    — показать весь словарь")
    print("  exit                    — выйти\n")

    while True:
        command = input("\nВведите команду: ").strip().lower()
        if command == "exit":
            print("До свидания!")
            break

        parts = command.split()
        if not parts:
            continue

        action = parts[0]

        if action == "add" and len(parts) >= 3:
            english = parts[1]
            french = parts[2]
            add_word(english, french)

        elif action == "remove" and len(parts) >= 2:
            english = parts[1]
            remove_word(english)

        elif action == "find" and len(parts) >= 2:
            english = parts[1]
            find_word(english)

        elif action == "replace" and len(parts) >= 3:
            english = parts[1]
            new_french = parts[2]
            replace_word(english, new_french)

        elif action == "show":
            show_all()

        else:
            print("Неверная команда. Попробуйте ещё раз.")
main()
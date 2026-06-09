def display_menu():
    print("\n" + "="*40)
    print("МЕНЮ СПРАВОЧНИКА")
    print("="*40)
    print("1. Отсортировать по идентификационным кодам")
    print("2. Отсортировать по номерам телефона")
    print("3. Вывести список пользователей с кодами и телефонами")
    print("4. Выход")
    print("-"*40)

def sort_by_ids(ids, phones):
    combined = sorted(zip(ids, phones), key=lambda x: x[0])
    ids[:], phones[:] = zip(*combined)
    print("Список отсортирован по идентификационным кодам.")

def sort_by_phones(ids, phones):
    combined = sorted(zip(ids, phones), key=lambda x: x[1])
    ids[:], phones[:] = zip(*combined)
    print("Список отсортирован по номерам телефона.")

def print_users(ids, phones):
    if not ids:
        print("Список пользователей пуст.")
        return
    
    print("\nСПИСОК ПОЛЬЗОВАТЕЛЕЙ:")
    for i, (user_id, phone) in enumerate(zip(ids, phones), 1):
        print(f"{i}. ID: {user_id}, Телефон: {phone}")

def main():
    identification_ids = [103, 101, 105, 102, 104]
    phone_numbers = [79161234567, 79167654321, 79165555555, 79169998877, 79161112233]
    
    while True:
        display_menu()
        choice = input("Выберите действие (1–4): ").strip()
        
        if choice == '1':
            sort_by_ids(identification_ids, phone_numbers)
        elif choice == '2':
            sort_by_phones(identification_ids, phone_numbers)
        elif choice == '3':
            print_users(identification_ids, phone_numbers)
        elif choice == '4':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")

main()


# -------------------------------------------------------------------------------------------------------------


def display_menu():
    print("МЕНЮ БИБЛИОТЕКИ")
    print("1. Отсортировать по названию книг")
    print("2. Отсортировать по годам выпуска")
    print("3. Вывести список книг с названиями и годами выпуска")
    print("4. Выход")

def sort_by_titles(titles, years):
    combined = sorted(zip(titles, years), key=lambda x: x[0].lower())
    titles[:], years[:] = zip(*combined)
    print("Список отсортирован по названиям книг.")

def sort_by_years(titles, years):
    combined = sorted(zip(titles, years), key=lambda x: x[1])
    titles[:], years[:] = zip(*combined)
    print("Список отсортирован по годам выпуска.")

def print_books(titles, years):
    if not titles:
        print("Список книг пуст.")
        return
    
    print("\nСПИСОК КНИГ:")
    for i, (title, year) in enumerate(zip(titles, years), 1):
        print(f"{i}. \"{title}\" — {year} год")

def main():
    book_titles = [
        "Мастер и Маргарита",
        "Преступление и наказание",
        "Война и мир",
        "1984",
        "Гарри Поттер и философский камень"
    ]
    book_years = [1966, 1866, 1869, 1949, 1997]
    
    while True:
        display_menu()
        choice = input("Выберите действие (1–4): ").strip()
        
        if choice == '1':
            sort_by_titles(book_titles, book_years)
        elif choice == '2':
            sort_by_years(book_titles, book_years)
        elif choice == '3':
            print_books(book_titles, book_years)
        elif choice == '4':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")

main()
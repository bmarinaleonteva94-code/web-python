books = {}

def add_book(book_id, author, title, genre, year, pages, publisher):
    if book_id in books:
        print(f"Книга с ID {book_id} уже существует.")
        return

    books[book_id] = {
        "author": author,
        "title": title,
        "genre": genre,
        "year": year,
        "pages": pages,
        "publisher": publisher
    }
    print(f"Книга '{title}' (ID: {book_id}) добавлена в коллекцию.")

def remove_book(book_id):
    if book_id in books:
        title = books[book_id]["title"]
        del books[book_id]
        print(f"Книга '{title}' (ID: {book_id}) удалена из коллекции.")
    else:
        print(f"Книга с ID {book_id} не найдена.")

def find_book(book_id):
    if book_id in books:
        book = books[book_id]
        print(f"  Данные книги (ID: {book_id}):")
        print(f"  Автор: {book['author']}")
        print(f"  Название: {book['title']}")
        print(f"  Жанр: {book['genre']}")
        print(f"  Год выпуска: {book['year']}")
        print(f"  Количество страниц: {book['pages']}")
        print(f"  Издательство: {book['publisher']}")
    else:
        print(f"Книга с ID {book_id} не найдена.")

def update_book(book_id, author=None, title=None, genre=None, year=None, pages=None, publisher=None):
    if book_id not in books:
        print(f"Книга с ID {book_id} не найдена.")
        return

    book = books[book_id]
    if author is not None:
        book["author"] = author
    if title is not None:
        book["title"] = title
    if genre is not None:
        book["genre"] = genre
    if year is not None:
        book["year"] = year
    if pages is not None:
        book["pages"] = pages
    if publisher is not None:
        book["publisher"] = publisher

    print(f"Данные книги {book_id} обновлены.")

def show_all_books():
    if not books:
        print("Коллекция пуста.")
        return

    print("\nВсе книги в коллекции:")
    for book_id, book in books.items():
        print(f"ID: {book_id} | Название: {book['title']} | Автор: {book['author']} | Год: {book['year']}")

def main():
    print("Программа «Книжная коллекция». Управление книгами.")
    print("Доступные команды:")
    print("  add <ID> <автор> <название> <жанр> <год> <страницы> <издательство> — добавить книгу")
    print("  remove <ID>                     — удалить книгу")
    print("  find <ID>                      — найти книгу")
    print("  update <ID> [поля]            — обновить данные (поля: author, title, genre, year, pages, pub)")
    print("  show                          — показать все книги")
    print("  exit                          — выйти\n")

    while True:
        command = input("\nВведите команду: ").strip()
        if not command:
            continue

        parts = command.split()
        action = parts[0].lower()

        if action == "exit":
            print("До свидания!")
            break

        elif action == "add" and len(parts) == 8:
            book_id = parts[1]
            author = parts[2]
            title = parts[3]
            genre = parts[4]
            year = parts[5]
            pages = parts[6]
            publisher = parts[7]
            add_book(book_id, author, title, genre, year, pages, publisher)

        elif action == "remove" and len(parts) == 2:
            book_id = parts[1]
            remove_book(book_id)

        elif action == "find" and len(parts) == 2:
            book_id = parts[1]
            find_book(book_id)

        elif action == "show":
            show_all_books()

        elif action == "update" and len(parts) >= 3:
            book_id = parts[1]
            updates = {}
            for arg in parts[2:]:
                if arg.startswith("author="):
                    updates["author"] = arg[7:]
                elif arg.startswith("title="):
                    updates["title"] = arg[6:]
                elif arg.startswith("genre="):
                    updates["genre"] = arg[6:]
                elif arg.startswith("year="):
                    updates["year"] = arg[5:]
                elif arg.startswith("pages="):
                    updates["pages"] = arg[6:]
                elif arg.startswith("pub="):
                    updates["publisher"] = arg[4:]

            update_book(book_id, **updates)

        else:
            print("Неверная команда. Проверьте синтаксис и количество аргументов.")


main()
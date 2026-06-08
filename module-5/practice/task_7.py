
def process_list(lst):
    if not lst: 
        return lst

    average = sum(lst) / len(lst)

    n = len(lst)

    if average > 0:
        two_thirds = n * 2 // 3
        sorted_part = sorted(lst[:two_thirds])
        remaining_part = lst[two_thirds:][::-1]
    else:
        one_third = n // 3
        sorted_part = sorted(lst[:one_third])
        remaining_part = lst[one_third:][::-1]

    return sorted_part + remaining_part

print(process_list([3, 1, 4, 1, 5, 9, 2, 6]))  
print(process_list([-3, -1, -4, -1, -5, -9, -2, -6]))

# ---------------------------------------------------------

def print_grades(grades):
    print("\nОценки студента:", ' '.join(map(str, grades)))


def retake_exam(grades):
    try:
        index = int(input("Введите номер оценки для пересдачи (1-10): ")) - 1
        if 0 <= index < len(grades):
            new_grade = int(input("Введите новую оценку (1-12): "))
            if 1 <= new_grade <= 12:
                grades[index] = new_grade
                print(f"Оценка №{index + 1} изменена на {new_grade}")
            else:
                print("Ошибка: оценка должна быть от 1 до 12!")
        else:
            print("Ошибка: номер оценки должен быть от 1 до 10!")
    except ValueError:
        print("Ошибка: введите целое число!")

def check_scholarship(grades):
    average = sum(grades) / len(grades)
    if average >= 10.7:
        print(f"\nСтипендия ВЫХОДИТ! Средний балл: {average:.2f}")
    else:
        print(f"\nСтипендия НЕ выходит. Средний балл: {average:.2f}")

def sort_grades(grades):
    choice = input("\nСортировка: 1 — по возрастанию, 2 — по убыванию: ")
    if choice == '1':
        sorted_grades = sorted(grades)
        print("Оценки по возрастанию:", ' '.join(map(str, sorted_grades)))
    elif choice == '2':
        sorted_grades = sorted(grades, reverse=True)
        print("Оценки по убыванию:", ' '.join(map(str, sorted_grades)))
    else:
        print("Неверный выбор!")

def main():
    print("Программа «Успеваемость»")
    print("Введите 10 оценок студента (от 1 до 12):")

    grades = []
    for i in range(10):
        while True:
            try:
                grade = int(input(f"Оценка {i + 1}: "))
                if 1 <= grade <= 12:
                    grades.append(grade)
                    break
                else:
                    print("Ошибка: оценка должна быть от 1 до 12! Попробуйте снова.")
            except ValueError:
                print("Ошибка: введите целое число!")

    while True:
        print("\n" + "="*40)
        print("МЕНЮ:")
        print("1 — Вывод оценок")
        print("2 — Пересдача экзамена")
        print("3 — Выходит ли стипендия?")
        print("4 — Вывод отсортированного списка оценок")
        print("0 — Выход")
        print("="*40)

        choice = input("Выберите действие (0-4): ")

        if choice == '0':
            print("До свидания!")
            break
        elif choice == '1':
            print_grades(grades)
        elif choice == '2':
            retake_exam(grades)
        elif choice == '3':
            check_scholarship(grades)
        elif choice == '4':
            sort_grades(grades)
        else:
            print("Неверный выбор! Попробуйте снова.")

main()


# ----------------------------------------------------------------

def improved_bubble_sort(arr):
    
    n = len(arr)
    print(f"Начальный список: {arr}")

    for pass_num in range(n - 1):  
        swaps = 0  
        print(f"\nПроход {pass_num + 1}:")

        for i in range(n - pass_num - 1):
            print(f"  Сравниваем {arr[i]} и {arr[i + 1]}")

            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                print(f"    Перестановка: {arr[i + 1]} ↔ {arr[i]} → {arr}")

        print(f"Количество перестановок на проходе {pass_num + 1}: {swaps}")

        if swaps == 0:
            print("Перестановок не было — список отсортирован!")
            break

    print(f"\nОтсортированный список: {arr}")
    return arr


def main():
    print("=== Усовершенствованная пузырьковая сортировка ===\n")

    try:
        user_input = input("Введите числа через пробел: ")
        numbers = list(map(int, user_input.split()))

        if not numbers:
            print("Ошибка: список пуст!")
            return

        sorted_numbers = improved_bubble_sort(numbers.copy())

        print("\n" + "="*50)
        print("Сортировка завершена!")

    except ValueError:
        print("Ошибка: введите только целые числа!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

main()


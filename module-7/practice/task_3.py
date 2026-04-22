with open("file1.txt", "r", encoding="utf-8") as f1, open("file2.txt", "r", encoding="utf-8") as f2:
    line_num = 1
    has_differences = False

    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        if not line1 and not line2:
            break
        clean_line1 = line1.rstrip('\n\r')
        clean_line2 = line2.rstrip('\n\r')

        if clean_line1 != clean_line2:
            print(f"Строка {line_num}: РАЗЛИЧИЕ")
            print(f"  Файл 1: '{clean_line1}'")
            print(f"  Файл 2: '{clean_line2}'")
            has_differences = True
        line_num += 1

    if not has_differences:
        print("Все строки в файлах полностью совпадают!")
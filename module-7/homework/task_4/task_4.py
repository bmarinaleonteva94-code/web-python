max_lenght = 0
with open ("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        current_lenght = len(line.rstrip("\n"))
        if max_lenght < current_lenght:
            max_lenght = current_lenght
    print(f"В самой длинной строке {max_lenght} символов")
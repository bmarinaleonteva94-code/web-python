with open("file.txt", "r", encoding="utf-8") as f:  
    lines = f.readlines()
    if lines:
        lines = lines[:-1]
    with open("file2.txt", 'w', encoding='utf-8') as f1:
        f1.writelines(lines)
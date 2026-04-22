search_word = input("Введите слово для поиска: ")
replace_word = input("Введите слово для замены: ")
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()
new_text = text.replace(search_word, replace_word)

with open("file.txt", "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Слово '{search_word}' заменено на '{replace_word}'")
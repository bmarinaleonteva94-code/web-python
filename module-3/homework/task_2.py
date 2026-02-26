text = input("Введите текст: ")
reserved_words = input("Введите зарезервированные слова: ").split()
for word in reserved_words:
    text = text.replace(word, word.upper())
print(text)
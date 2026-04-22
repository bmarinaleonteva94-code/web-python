word = input("Введите слово, которое необходимо посчитать: ")
count = 0
with open ("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        words = line.strip().replace(".", "").replace(",", "").replace("?", "").replace("!", "").lower().split()
        count += words.count(word.lower())

print(count)
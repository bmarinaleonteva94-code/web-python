str = input("Введите любое слово: ")
d = {}
for word in str:
    d.setdefault(word, 0)
    d[word] += 1
print(d.items())
for key, value in d.items():
    print(f"{key} = {value}")
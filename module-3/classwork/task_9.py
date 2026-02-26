text = "it has survived not only five centuries 12345. but also the leap into electronic typesetting, remaining essentially unchanged."
sentences = text.split(". ")
new_text = ". ".join([s.capitalize() for s in sentences])

count_digit = 0
for char in text:
    if char.isdigit():
        count_digit += 1


print(new_text)
print(f"Количество цифр в тексте: {count_digit}")
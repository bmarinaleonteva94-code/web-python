def func(text):
    text = text.replace(" ", "")
    max_count = 0
    char_result = ''
    for char in text:
        count = text.count(char)
        if count > max_count:
            max_count = count
            char_result = char
    return char_result

print(func("dddd ff ggg w"))
print(func("hello"))
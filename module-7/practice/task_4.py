input_filename = 'file.txt'
output_filename = 'statistics.txt'

vowels = set('aeiouAEIOUаяуюэеыиоАЯУЮЭЕЫИО')
digits = set('0123456789')

char_count = 0
line_count = 0
vowel_count = 0
consonant_count = 0
digit_count = 0

with open(input_filename, 'r', encoding='utf-8') as file:
    for line in file:
        line_count += 1
        char_count += len(line)
        for char in line:
            if char.isalpha():  
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
            elif char in digits: 
                digit_count += 1

with open(output_filename, 'w', encoding='utf-8') as output_file:
    output_file.write(f"Количество символов: {char_count}\n")
    output_file.write(f"Количество строк: {line_count}\n")
    output_file.write(f"Количество гласных букв: {vowel_count}\n")
    output_file.write(f"Количество согласных букв: {consonant_count}\n")
    output_file.write(f"Количество цифр: {digit_count}\n")
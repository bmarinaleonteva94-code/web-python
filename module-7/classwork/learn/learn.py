# file = open("file.txt", "r")
# # print(file.read())       # выводит весь файл
# print(file.read(1))    # выводит первый символ
# file.close()     # закрывает поток(файл)

#  r - чтение 
#  w - запись с очисткой предыдущего файла
#  a - append, добавится новый текст в конец файла
#  x - создает новый файл, если такой файл уже существует, то выдаст ошибку
#  t - работа в текстовом режиме
#  b - бинарный режим: картинки, музыка, видео
#  + - одновременное чтение и запись файла
#  ----------------------------------------------------------------------
#  file = open("C:\Windows")      выдаст ошибку, так как \ - символ экранирования
#  file = open("C:\\Windows")       для решения проблемы нужно добавить дополнительный \
#  file = open("C:/Windows")      лучший способ указать адрес


# file = open("file.txt", "w")
# file.write("54321")
# file.close()

# file = open("file.txt", "a")
# file.write("-добавили в конец")    # вопросительные знаки вместо русских букв, для решения добавляется кодировка
# file.close()

# file = open("file.txt", "a", encoding="utf-8")
# file.write("-добавили в конец")    # вопросительные знаки вместо русских букв, для решения добавляется кодировка
# file.close()



# f = open("file1.txt", "a", encoding="utf-8")
# f.write("1,2,3\n")              
# f.write("4,5,6\n")
# f.write("7,8,9")
# f.close()

# f = open("file1.txt", "r", encoding="utf-8")      # чтение всего файла
# print(f.readline().strip())
# print(f.readline().strip())
# f.close()

# for line in f:           # чтение всего файла
#     print(line.strip())    
# f.close()

with open("file1.txt", "r", encoding="utf-8") as f:    # чтение всего файла
    for line in f:
        print(line.strip())
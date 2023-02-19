# f = open("суперультрапупер секретный файл.txt", "w", encoding="utf 8")  # создаст если нет, перезапишет если есть
# f.write("hello world\n")
# f.write("hello world")
# f.close()

# f = open("суперультрапупер секретный файл.txt", "r", encoding="utf 8")
# #contend = f.read() # ЛИБО ТАК # считываем содержимое файла
# contend = f.readlines() # ЛИБО ТАК
# print(contend)
# for logarifm in contend:
#     print(logarifm.rstrip())
# f.close()


# ЗАДАЧА 1
nazvanie = input("Введите название файла --> ")
f = open(nazvanie + ".txt", "w", encoding="utf-8")
while True:
    text = input("Введите текст --> ")
    f.write(text + "\n")
    if text == " ":
        break
f.close()


# ЗАДАЧА 2
# nazvanie = input("Введите название файла --> ")
# f = open(nazvanie, "r", encoding="utf 8")
# content = f.readlines()
# print(content)
# v = len(content)
# for i in range(v):
#     print(f"{i+1})",content[i].strip())
#
#
# # ЗАДАЧА 3
# f = open("zxc.txt", "r", encoding="utf-8")
# text = f.readlines()
# f.close()
# count = 0
# while text != []: # пока не вытащены все линии
#     elements = text[:3]
#     count += 1
#     f = open(str(count) + ".txt", "w", encoding="utf-8")
#     for i in elements: # элемент из троек
#         f.write(i)
#     f.close()
#     del text[:3]
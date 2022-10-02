# # #x = ["A", "Б", "В", "Г", "Д", "Е", "Ё", "Ж" ]
# # x = "Мама мыла раму"
# # print("Последний элемент =", x[-1])
# # print("Первый элемент =", x[0])
# # print("Первые 5 элементов =", x[0:5])
# # print("Первые 5 элементов через одного =", x[0:5:2])
#
# ##строка - это не изменяемый тип данных
# #x = "прювет"
# #x[2] = "и"  #так нельзя
#
# # x = "я белогородский купольщик, я карта, я антон"
# # print(x[-5:])
# # print(x[:25])
# x = input("Введи слово:")
# temp = x[-1]
# index = x.index(temp)
# #print(index + 1)
# print(len(x))

# path = "C:/Python/python.exe"
# # print("Имя файла:", path[-10:])
# # print("Расширение", path[-3:])
# # print("Имя каталога:", path[3:10])
# # print("Полный путь к каталогу", path[0:10])
#
# path_2 = path.split("/")
# print(path_2)
#
# print("Имя файла:", path_2[-1])
# print("Расширение", path_2[-1][-3:])
# print("Имя каталога:", path_2[1])
# print(f"Полный путь к каталогу, {path_2[0]}/{path_2[1]}")

# chapter_1 = input("Глава 1:")
# page_1 = input("Страница :")
#
# chapter_2 = input("Глава 2:")
# page_2 = input("Страница :")
#
# chapter_3 = input("Глава 3:")
# page_3 = input("Страница :")
# print(chapter_1.ljust(15), page_1.rjust(15))
# print(chapter_2.ljust(15), page_2.rjust(15))
# print(chapter_3.ljust(15), page_3.rjust(15))
x = "12'345'678"
# РЕШЕНИЕ ЧЕРЕЗ .SPLIT
# temp = x.split("'")             -- одно из решений
# print(temp)
# number = int(temp[0] + temp[1] + temp[2])
# print(number)

# РЕШЕНИЕ ЧЕРЕЗ []
# temp = x[0:2] + x[3:6] + x[-3:]
# number = int(temp)
# print(temp)
# РЕШЕНИЕ ЧЕРЕЗ .REPLASE
# temp = x.replace("'", "")
# print(temp)

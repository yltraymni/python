x = 7
# if x >= 10:   # больше или равно
#     print("Я сработал!")
# else:
#     print("Ну я тоже сработал")
#
# phrase = "Я карта"
# if phrase == "ya karta":   # равно ли
#     print("Мы карты!")
# else:
#     print()
#
#
# game = "dota2"
# if game != "brawl stars":     # не равно
#     print("ну можно и поиграть")
#
# x = 7
# if x >= 10 and (x == 0 or x == 666):
#     print("Я не выполнюсь хоть ошибок и нет")
# else:
#     print("Ну я тоже сработал")
#
# number = int(input("Введите число: "))
# if number > 0:
#     print("Положительное")
# elif number == 0:  # elif = else if (иначе если)
#     print("Нулик")
# else:
#     print("Отрицательное")
#
# year = int(input("Введите год: "))
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print("Високосный год")
# else:
#     print("Не високосный год")
#
# number_1 = int(input("Введи первое число: "))
# operation = input("Введи оперцию(-, +, *, /):").strip()  # ввод операции
# # убрать пробелы
# number_2 = int(input("Введи второе число"))
# lst = ["-", "+", "*", "/"]   # список допустимых символов
#
# if operation in lst:
#     if operation == "-":
#         print(number_1 - number_2)
#     elif operation == "+":
#         print(number_1 + number_2)
#     elif operation == "*":
#         print(number_1 * number_2)
#     else:
#         print(number_1 / number_2)

# number_1 = int(input("Введи первое число: "))
# number_2 = int(input("Введи второе число: "))
# number_3 = int(input("Введи третье число: "))
#
# counter_pol = 0 # счетчик положительных
# counter_otr = 0 # счетчик отрицательных
# # проверка первого числа
# if number_1 < 0:
#     counter_otr += 1 # прибавить к отрицательным
# else:
#     counter_pol += 1 # прибавить к положительным
#
# # проверка второго числа
# if number_2 < 0:
#     counter_otr += 1 # прибавить к отрицательным
# else:
#     counter_pol += 1 # прибавить к положительным
#
# # проверка третьего числа
# if number_3 < 0:
#     counter_otr += 1 # прибавить к отрицательным
# else:
#     counter_pol += 1 # прибавить к положительным
#
#
# print("Положительных:", counter_pol)
# print("Отрицательных:", counter_otr)
#
# number_1 = int(input("Введи первое число: "))
# number_2 = int(input("Введи второе число: "))
# number_3 = int(input("Введи третье число: "))
#
# lst = [number_1, number_2, number_3]
#
# maxi = max(lst)
# mini = min(lst)
# print("Минимальное:", mini)
# print("Максимальное", maxi)

ticket = input("Введите номер билета(6 знаков):")
if len(ticket) == 6 and ticket.isdigit(): # число ли это(в формате str)
    first_half = ticket[:3]  # сохраняем первые три числа
    last_half = ticket [-3:]  # сохраняем последние три числа

    first_sum = first_half[0] + first_half[1] + first_half[2]
    last_sum = last_half[0] + last_half[1] + last_half[2]

    if first_sum == last_sum:
        print("красава жестка")
    else:
        print("ливай попущь")
else: # если ввод некоректный
    print("Нормально общайся ээЭЭ")











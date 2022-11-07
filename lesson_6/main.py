# month = input("Введите номер месяца: ")
# if month.isdigit() and 1 <= int(month) <= 12:  # .isdigit() - число ли
#     month = int(month)
#     if 3 <= month <= 5 :
#         print("Весна")
#     elif 6 <= month <= 8:
#         print("Лето")
#     elif 9 <= month <= 11:
#         print("Осень")
#     else:
#         print("Зима")
# else:
#     print("Это не число")

# h = int(input("Часы: "))
# m = int(input("Минуты: "))
# s = int(input("Секунды: "))
#
# if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
#     print("Формат правильный: ")
#     print(f"{h}:{m}:{s}")
# else:
#     print("Ошибка")
#     if h > 23 or h < 0: # если ошибка в часах
#         print("Часы в формате [0, 23]")
#     if m > 59 or m < 0: #
#         print("Минуты в формате [0, 59]")
#     if s > 59 or s < 0:
#         print("Секунды в формате [0, 59]")
count = 0
q1 = input("Какого цвета трава?\n"
           "a)Голубая ,б)60 бойцов, в)Венера, г)Зеленая\n"
           "--> ")
if q1 == "г":
    count += 1
    print("Правильно!")
else:
    print("Ты ошибся")
    print("Твоё колличество очков:", count)
    #quit()

q2 = input("Сколько ног у паука \n"
           "a)Шесть, б)Семь, в)Восемь, г)Девять\n"
           "--> ")
if q2 == "в":
    count += 1
    print("Правильно!")
else:
    print("Ты ошибся")
    print("Твоё колличество очков:", count)
    quit()

q3 = input("Сколько метров тунель может прорыть крот за одну ночь?\n"
           "а)76, б)8, в)100, г)150\n"
           "--> ")
if q3 == "а":
    count += 1
    print("Правильно!")
else:
    print("Ты ошибся")
    print("Твоё колличество очков:", count)
    quit()


q4 = input("Сколько iq у среднестатистического человека?\n"
           "a)90, б)100, в)50, г)150\n"
           "--> ")
if q4 == "б":
    count += 1
    print("Верно")
    print("Твое колличество очков: ", count)
else:
    print("Ты ошибся")
    print("Твоё колличество очков: ", count)
    quit()
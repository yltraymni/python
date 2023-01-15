# def hello_world():
#     print("Hello world")
#
#
# hello_world()


# def plus(number_1, number_2):
#     result = number_1 + number_2
#     return result
#
# x = plus(5, 4)  # вызов функции с аргументом. результат записан в переменную
# plus(number_2=3, number_1=23)

# def is_danil(name):
#     if name == "Данил":
#         return True
#
#
# if is_danil("Данил"):  # если функция вернет True
#     print("Это Данил")
# else:
#     print("Это не Данил")

# ЗАДАЧА_1

# def if_sorted(list):
#     sort = sorted(list)
#     if list == sort:
#         return True
#
#
#
# list = [1, 4, 8, 13, 18]
# if if_sorted(list):
#     print("Список отсортирован")
# else:
#     print("Список не отсортирован")


# ЗАДАЧА_2

# def find_longest(list):
#     spisok2 = []
#     for i in list:
#         spisok2.append(len(i))
#     maxy = max(spisok2)
#     ind = spisok2.index(maxy)
#     return list[ind], spisok2[ind]
#
#
#
# spisok = ["Пудж", "Мангол", "zxc", "Дверь", "Дом"]
# spisok2 = []
# print(find_longest(spisok))
#


# ЗАДАЧА_3

# def min_max(chisla):
#     mini = chisla[0]
#     maxi = chisla[0]
#     for i in chisla:
#         if i > maxi:
#             maxi = i
#         elif i < mini:
#             mini = i
#     return maxi, mini
#
#
#
#
#
#
# chisla = [1, 3, 5, 8, 12, 56]
# print(min_max(chisla))


# ЗАДАЧА_1

# def is_prime(chislo):
#     for i in range(2, chislo+1):
#         if i == chislo:
#             return True
#         if chislo % i == 0:
#             break
#
#
#
#
#
#
# if is_prime(7):
#     print("Простое")
# else:
#     print("сложное")


# ЗАДАЧА_6

# def join(spisok:list, razdelitel:str)->str:
#     result = ""
#     for i in spisok:
#         result += i + razdelitel
#     return result
#
#
#
#
# list = ["Пудж","Пак", "SF"]
# print(join(list, "|"))

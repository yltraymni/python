# ZeroDivisionError:
# print(55/0)

# TypeError:
# x = 1 + "один"

# IndexError:
# lst = ["один", 2, "Антон"]
# lst[3]

# SyntaxError:
# if 5 < 0

# NameError:
# print(x)

# exit code:
# 0 - все хорошо
# 1 - ошибка
# -1 - прерывание программы

# try:  # попытаться
#     number = int(input("Введи число: "))
#     x = 5 / number
#     print(x)
# except ZeroDivisionError: # ловим исключеня
#     print("на ноль делить нельзя клоуняра")
# except ValueError: # если введем буквы
#     print("цифрами пиши анскил")
# except Exception: # обработка любой ошибки
#     print("Ошибка:-(")
# try:
#     name = input("Введите имя: ")
#     if name == "верните соску":
#         raise Exception("это имя занято ботискафыч")
# except Exception as error_m:   # складываем исключение в error_m
#     print("Запрещаю", error_m)
# else:   # иначе(если не вызывались исключения)
#     print("Такое имя разрешено")
# finally: # сработает в любом случае
#     print("ы")
# try:
#     number = int(input("Введите число"))
#     x = 5 / number
# except Exception:
#     pass   # затычка, заглушка
#
# if 3 == 3:
#     pass # TODO: не забудь дописать и купить молока
#
# temperature = 365 # коментарий
# print ()

def summa(numbers):
    return sum(numbers)


print(summa([1, 2, 3]))
assert  summa([1, 2]) == 3
assert  summa([1, 2]) == 4

# AssertionError - ошибка если не прошли проверку



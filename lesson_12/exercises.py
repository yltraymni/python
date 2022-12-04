# a = int(input("a: "))
# b = int(input("b: "))
# lst = []
#
# for aaa in range(a + 1, b):
#     lst.append(aaa ** 2)
# print(lst)

# x = input("Ввод: ")
# lst = x.split(" ")
# lst.reverse()
# print(lst)

# number = ""
# chet = 0
# nechet = 0
# lst = []
# while number != "end":
#     number = input("Число: ")
#     if number.lstrip("-").isdigit():  # .lstrip("-") - удалить минус слева
#         number = int(number)
#         lst.append(number)
#     elif number == "end":
#         break # выход из цикла
#     else:
#         print("Введи число:")
#         continue # перезапускает цикл
#
#     if number % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1
# print(lst)
# print(f"Четные: {chet}шт")
# print(f"Нечетные: {nechet}шт")


lst = [-5, -8, 2, 14, 1]
mini = min(lst)
maxi = max(lst)


lst[lst.index(mini)], lst[lst.index(maxi)] = lst[lst.index(maxi)], lst[lst.index(mini)]
print(lst)

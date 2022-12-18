# a = [1,2,3,4]
# b = [7,2,3,8]
# index = 0
# count = 0
#
# while True:
#     if a[index] == b[index]:
#         count += 1
#         index += 1
#         print(count)
#         break

# a = [0, 7, 14, 28, 0, 7, 1, 2, 3, 123]
# b = [2, 4, 1, 78, 28, 14, 2, 43, 123]
# a_set = set(a)
# b_set = set(b)
# x = list(a_set & b_set)
# x.sort()
# print(x)
# lst = []
# a = [3, 1, 4, 2, 65, 23, 2, 76, 65, 3]
#
# for i in a:
#     if i in lst:
#         print("YES")
#     else:
#         lst.append(i)
#         print("NO")
# a = [1, 2, 3, 1000000000, 123, 76, 43, 6, 9]
# m = a[0]
# for i in a:
#     if i < m:
#         m = i
# print(m)
# lst1 = []
# lst = []
# a = [1, 7, 2, 12, 2, 45, 7]
# for i in a:
#     if i in a:


# СЛОВАРЮ

# dict1 = {"Ключ1": 1.2,
#         "Ключ2 : Антон", "Якрут" : "True", "Словарь" : {}}


# ЦИКЛЫ
# x = 5
# while True:
#     print(123)
# while False: # условие невыполнимо
#     print("Бака")
#
# phrase = "фраза"
# for i in phrase:
#     print(i)
#
# for jojo in range(5):
#     print(jojo)


# МНОЖЕСТВА
# set1 = dict()  # единственный способ создания пустого множества
# set2 = {1, 2, 3, 4}  # литеральный способ
# set = {1, 1, 1, 2}  # повторения исключены
# print(set)
# set0 = {"А", "Б", "Ц"}  # неупорядоченный тип данных
# print(set0)
# set00 = {1, [2, 3]}
# # TypeError -> Нельзя помещать изменяемые типы данных во множество
#
# # Немутабельные типы данных = неизменняемые
# # int, float, bool, str, tuple

# # Оперции на множествах
# set1 = {1, 2, 3, 4, 5,}
# set2 = {3, 4, 5, 6, 7}
#
# # Объединение
# print(set1.union(set2))
# print(set1 | set2)
#
# # Пересечение
# print(set1.intersection(set2))
# print(set1 & set2)  # амперсанд
#
# # Разность
# print(set1.difference(set2))
# print(set1 - set2)
#
# # Симмертрическая разность
# print(set1.symmetric_difference(set2))
# print(set1 ^ set2)

#
# from random import randint
# lst = []
# for _ in range(5):
#     lst.append(randint(1, 5))
#     lst1_set = set(lst)
#     count = len(lst1_set)
# print(lst)
# print(f"{count} штук: {lst1_set}")

from random import randint

r_start = 0
r_end = 10_000  # 10_000 то же самое что и 10000
size = randint(100, 1000)









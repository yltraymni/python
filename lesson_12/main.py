# мутаельность
# мутабельные - изменяемые
# немутабельные - неизменяемые




# lst = ["один", "два", "попит"]
# lst.append("спинер")  # .append() - добавить по индексу
# lst.pop(0)  #.pop() - удалить по индексу
# lst.remove("два")  # .remove() - удалить по значению

# lst = [0, 3, 5, -2, 1]
# lst.reverse() # .reverse() - отразить, перевернуть
# print(lst)

# lst1 = [0, 1, 2]
# lst2 = [3, 4, 5]
# lst1.extend(lst2)  # .extend() - расширите
# print(lst1)

# lst = [1, 2]
# lst.insert(1, 1.5)  # .insert() - вставить по индексу
#
# lst = ["чоо случилось"]  -> []
# lst.clear()  # .clear() - очистка

# lst = [0, 4, 2, -5, 1]
# lst.sort()  # .sort() -  сортировка
# lst.sort(reverse=True)  # reverse=True от меньшего к большему

# котреж
# tup  = (1, 2, 3)
# tup = 1, 2, 3
# tup = 1,
#
# print(max(tup))
# print(min(tup))

# list1 = ["A", "B", "C"]
# list2 = ["1", "1", "2"]
# coupl = zip(list1, list2)  # zip() - функция склеивания по индексам
#
# for x in coupl:
#     print(x)

from collections import namedtuple
citizen = namedtuple("Житель", "имя возраст статус")
alex = citizen(имя="Леха Денжер", возраст="27", статус="Предприниматель")
print(alex.имя)
print(alex.статус)
print(alex.возраст)


# alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТ"
# print(alphabet[::-2]) # вывод в обратном порядке
# #[сарт:конец:шаг]

# phrase = "антон"
# print(phrase.upper())  # поднять в верхний регистр
# print(phrase.lower())  # опустить в нижний регистр
#
# phrase1 = "зОлотыЕ купола, Я тоП рИкимару миРа, не бери инвокера"
# print(phrase1.capitalize())  # нормализует текст, в стандартную форму

# familiya = input("Фамилия: ").capitalize()
# imya = input("Имя: ").capitalize()
# otchestvo = input("Отчество: ").capitalize()
# print(familiya, imya[0] + ".", otchestvo[0] + ".")
# print(f"{familiya} {imya[0]}. {otchestvo[0]}.")

# x = input()
# print(x.count("a"))
# print(x.lower().count("a"))  # кол-во маленьких "а"

# x = input("Введите фразу, разделяя слова запятыми: ")
# lst = x.split(",")
#       # .remove("Вова") - удалить элемент
#       # .pop(3) - удалить элемент под индексом 3
# lst.pop(0)
# print(lst)  # split - разделить, расколоть

# phrase = input("Введите фразу: ")
# find = input("Что меняем: ")
# replace = input("На что меняем: ")
# print(phrase.replace(find, replace))

# phrase = input("Введите фразу: ")
# print(phrase.replace("йо", "ё"))
# alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТ"
# print(alphabet[::-2]) # вывод в обратном порядке
# #[сарт:конец:шаг]

# phrase = "антон"
# print(phrase.upper())  # поднять в верхний регистр
# print(phrase.lower())  # опустить в нижний регистр
#
# phrase1 = "зОлотыЕ купола, Я тоП рИкимару миРа, не бери инвокера"
# print(phrase1.capitalize())  # нормализует текст, в стандартную форму

# familiya = input("Фамилия: ").capitalize()
# imya = input("Имя: ").capitalize()
# otchestvo = input("Отчество: ").capitalize()
# print(familiya, imya[0] + ".", otchestvo[0] + ".")
# print(f"{familiya} {imya[0]}. {otchestvo[0]}.")

# x = input()
# print(x.count("a"))
# print(x.lower().count("a"))  # кол-во маленьких "а"

# x = input("Введите фразу, разделяя слова запятыми: ")
# lst = x.split(",")
#       # .remove("Вова") - удалить элемент
#       # .pop(3) - удалить элемент под индексом 3
# lst.pop(0)
# print(lst)  # split - разделить, расколоть

# phrase = input("Введите фразу: ")
# find = input("Что меняем: ")
# replace = input("На что меняем: ")
# print(phrase.replace(find, replace))

# phrase = input("Введите фразу: ")
# print(phrase.replace("йо", "ё"))
# alphabet = {
#     "а":"a",
#     " ":" ",
#     "б":"b",
#     "в":"v",
#     "г":"g",
#     "д":"d",
#     "е":"e",
#     "ё":"yo",
#     "ж":"zh",
#     "з":"z",
#     "и":"i",
#     "й":"io",
#     "к":"k",
#     "л":"l",
#     "м":"m",
#     "н":"n",
#     "о":"o",
#     "п":"p",
#     "р":"r",
#     "с":"s",
#     "т":"t",
#     "у":"u",
#     "ф":"f",
#     "х":"h",
#     "ц":"c",
#     "ш":"sh",
#     "я":"ia",
#     "щ":"sch",
#     "ы":"i",
#     "ю":"iu",
#
# }
# x = input("Введите фразу для транслитерации: ")
# rus = ""
# for letter in x:
#     rus = rus + alphabet[letter]
# print(rus)

# alphabet = {
#     "а":"a",
#     "б":"b",
#     "в":"v",
#     "г":"g",
#     "д":"d",
# }
# x = input("Введите фразу чего-то: ")
# rus = ""
# for bukva in x:
#     rus = rus + alphabet[bukva]
# print(rus)


email = input("Введите почту: ")
print(email.split("@"))
login = email.split("@")[0]
domain = email.split("@")[-1]
print("login:", login)
print("Домэн:", domain)
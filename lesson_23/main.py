# class Person:
#     def __init__(self, name, age):  # МАГИЧЕСКИЙ МЕТОД (ИНИЦИАЛИЗАЦИИ)
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Я {self.name}, мне {self.age} лет"
# chelovek = Person("Данис", 29)  # создание объекта класса Person
# chelovek1 = Person("Виталя", 34)  # создание объекта класса Person
#
# print(chelovek.name)
# print(chelovek1.name)
# # print(chelovek)
# print(str(chelovek1))
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        return f"Имя: {self.name};\nВозраст: {self.surname};\nФамилия: {self.age}."
    def greet(self):
        return f"Привет! Меня зовут {self.surname} {self.name}, мне {self.age} лет"
chel = Person("Володя", "Приколов", 16)
print(chel.name, chel.surname, chel.age)
print(chel)
print(chel.greet())


# ЗАДАЧА 2
# nums = [random.randint(2, 5) for _ in range(random.randint(5, 10))]
# print(nums)
class Person:
    def __init__(self, imyau, familia, voz):
        self.name = imyau
        self.femiliya = familia
        self.vozrast = voz
        self.grades = [random.randint(2, 5) for _ in
                       range(random.randint(5, 10))]
        self.srbal = sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Возраст: {self.vozrast}\nИмя: {self.name}\nФамилия: {self.femiliya}"

    def greet(self):
        return f"Привет, меня зовут {self.name}, мне {self.vozrast} лет."


chel = Person("Антон", "Бананов", 15)
chel2 = Person("Володя", "Приколов", 17)
print(chel.grades, chel.srbal)


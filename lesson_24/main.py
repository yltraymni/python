# class Human:
#     def __init__(self):   # инициализация (магический метод)
#         self.haight = 993  # public данные
#         self.__money = 0.3  # ptivate данные
#     def zdarov(self):  # обычный метод
#         return "Приветствую"
#
#     def ipoteka(self):
#         if self.__money > 50 and self.__normal_haight():
#             return True
#         else:
#             return False
#     def __normal_haight(self):
#         if 100 < self.haight < 200:
#             return True
# chel = Human()
# # print(chel.haight)  # вызов атрибута
# # print(chel.zdarov())  # вызов метода
#
# print(chel.haight)  # public можно выводить
# chel.haight += 7  # public можно менять
#
# #print(chel.__money)  # private нельзя выводить
# chel.__money = 5  # private менять нельзя
# print(chel.__money)
# chel._Human__money += 5
#
# class Car:
#     def __init__(self):
#         self.statys = False
#     def start(self, statys):
#         if not self.statys:
#             self.statys = True
#             return "Автомобиль заведен"
#         else:
#             return "Она уже заведена"
#     def stop(self, statys):
#         if not self.statys:
#             self.statys = True
#             return "Автомобиль заглушен"
#         else:
#             return "Он уже заглушен"
#     def year(self, god):
#         self.year = god
#     def type(self, tip):
#         self.type = tip
#     def color(self, cvet):
#         self.color = cvet
# mach = Car()
# mach.color("желтый")
# mach.type("грузовой")
# mach.year(2012)
# print(mach.start(), mach.stop())

# import string
# class Alphabet:
#     def __init__(self):
#         self.__lang = "eng"
#         self.__letter = string.ascii_lowercase
#     def print(self):
#         return self.__letter
#     def letters_num(self):
#         return len(self.__letter)
#
#
# a = Alphabet()
# print(a.print())
# print(a.letters_num())


# ЗАДАЧА 3
import datetime
class Watch:
    def __init__(self):
        self.__h, self.__m, self.__s = datetime.datetime.now().strftime("%H:%M:%S").split(":")
        self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)
    def minits(self):
        self.__m += 1
    def hour(self):
        self.__h += 1
    def second(self):
        self.__s += 1
    def retyrn(self):
        return f"{str(self.__h).rjust(2, '0')}:{str(self.__m).rjust(2, '0')}:{str(self.__s).rjust(2, '0')}"
time_now = Watch()
time_now.hour()
print(time_now.retyrn())




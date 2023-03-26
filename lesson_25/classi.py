# class Anton:
#     location = "Новосибирск"  # public static
#     # __Location = "Новосибирск"  # private static
#     def __init__(self, rost=1, ves=50,):  # __magic__
#         self.height = rost  # public dynamic
#         self.__weight = ves  # private dynamic
#         self.otkyda = Anton.location  # Использование статики
#     def __private(self):
#         pass
#
#     def public(self):
#         pass
#
# chelovek = Anton(123)
# print(chelovek.height)
# print(chelovek.weight)
import math
import random
class Human:
    default_name = "Данил"
    default_age = 25
    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 1000
        self.__house = None
    def info(self):
        return self.name, self.age, self.__house, self.__money

    def earn_money(self):
        __plus = 10000
        self.__money += __plus
        return __plus

    def default_info(self):
        return Human.default_name, Human.default_age

    def __make_deal(self, dom):
        if self.__money >= dom.final_price():
            self.__money -= dom.final_price()
            return True

    def buy_house(self, dom):
        if self.__make_deal(dom):
            dom.owner = self.name
            self.__house = dom
        else:
            skolko_raz = math.ceil((dom.final_price() - self.__money) // self.earn_money())
            for i in range(skolko_raz):
                self.earn_money()
            return f"Деньги подняты. На работу сходил {skolko_raz}раз"

class House:
    def __init__(self, adres, price):
        self.__area = adres
        self.__price = price
        self.skidka = random.randint(5, 25)

    def final_price(self):
        return self.__price - self.skidka / 100 * self.__price

chelovek = Human()
dom = House("91/2", 2000000)
print(chelovek.buy_house(dom))
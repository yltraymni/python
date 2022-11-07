import random
import time
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
figures = [rock, paper, scissors]
# rock = "камень"
# paper = "бумага"
# scissors = "ножницы"
time.sleep(0.5)
print("Давай сыграем")
time.sleep(0.5)
chp = int(input("Выберете: бумага - 1, камень - 2, ножницы - 3||    "))
chc = random.choice(figures)
print("У компьютера ", chc)


if chp == 3 and chc == scissors:
    print("Ничья😶😶😶")
if chp == 2 and chc == rock:
    print("Ничья😶😶😶")
if chp == 1 and chc == paper:
    print("Ничья😶😶😶")
if chp == 1 and chc == rock:
    print("Вы выигали🥳🥳🥳")
if chp == 2 and chc == paper:
    print("Вы проиграли😥😥😥")
if chp == 3 and chc == paper:
    print("Вы выигали🥳🥳🥳")
if chp == 1 and chc == scissors:
    print("Вы проиграли😥😥😥")
if chp == 2 and chc == scissors:
    print("Вы выигали🥳🥳🥳")
if chp == 3 and chc == rock:
    print("Вы проиграли😥😥😥")






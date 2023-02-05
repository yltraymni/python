import easygui
import random


def rock_paper_scissors():
    b = "img/бумага.png"
    k = "img/камень.png"
    n = "img/ножницы.png"
    user_choice = easygui.buttonbox(
        images= [k, n, b],
        choices= ("Выйти",)
    )
    computer_choice = random.choice([k, n, b])

    if user_choice == b and computer_choice == b:
        easygui.msgbox(msg="Ничья")
    elif user_choice == b and computer_choice == k:
        easygui.msgbox(msg="Вы выйграли")
    elif user_choice == b and computer_choice == n:
        easygui.msgbox(msg="Вы проиграли")
    elif user_choice == k and computer_choice == k:
        easygui.msgbox(msg="Ничья")
    elif user_choice == k and computer_choice == n:
        easygui.msgbox(msg="Вы выйграли")
    elif user_choice == k and computer_choice == b:
        easygui.msgbox(msg="Вы проиграли")
    elif user_choice == n and computer_choice == n:
        easygui.msgbox(msg="Ничья")
    elif user_choice == n and computer_choice == k:
        easygui.msgbox(msg="Вы проиграли")

        easygui.msgbox(msg="Вы выйграли")
    print(user_choice, computer_choice)


def guess_the_number():
    chislo = random.randint(1, 100)
    user = easygui.integerbox(
        msg = "Отгадай число от 1 до 100",
        upperbound=100,
        lowerbound = 1
    )
    while user != chislo:
        if user > chislo:
            user = easygui.integerbox(msg = f"Нужно число меньше чем {user}", upperbound=100,lowerbound = 1, image = "img/меньше.png")
        elif user < chislo:
            user = easygui.integerbox(msg=f"Нужно число больше чем {user}", upperbound=100, lowerbound=1, image="img/больше.png")
    user = easygui.msgbox(msg="Число отгадано", image = "img/apple.png")
games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()

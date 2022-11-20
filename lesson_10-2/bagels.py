import random

life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)  # число -> строчку

while life:  # то же самое, что и while life != 0
    is_guessed = False  # отгадано?
    print("=" * 10)

    print("Жизней:", end="")
    for _ in range(life):
        print("❤", end="")
    print( )

    guess = input("Предположение: ")
    if len(guess) != length or not guess.isdigit():  # если длина != 3 или не число
        print("Число от 100 до 999, пожалуйста!")
        continue
    # проверка правльного ответа
    if guess == answer:
        print("Победа 🏆")
        is_guessed = True
        break # выйти из цикла while

    if is_guessed == False:  # если не отгадано
        # проверка на fermi
        for i in range(length):
            if guess[i] == answer[i]:
                print("Fermi 😎")
                is_guessed = True
                break  # выход из цикла for

    if is_guessed == False:  # если не отгадано и не fermi
        # проверка на pico
        for char in guess:
            if char in answer: # есть ли число в ответе
                print("Pico 😉")
                is_guessed = True
                break

    if is_guessed == False:  # если не отгадано и не fermi и не pico
        print("Bagels ☹")

    life -= 1
print(answer)










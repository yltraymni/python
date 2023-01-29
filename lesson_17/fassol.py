def beans(x:int):  # отнимает фасоль
    global fassol
    fassol -= x

fassol = 20
while True:

    # ХОД 1 ИГРОКА
    while True: # проверка корректности
        first = int(input("1, 2, 3 боба "))
        if first <= 3 and first >= 1:
            break
    beans(first)
    if fassol < 1:
        print("Первый выйграл")
        if fassol == 1:
            print("Первый победил")
        elif fassol == 1:
            print("Второй выйграл")
            break
        else:
            print(f"{fassol} фасоли")
    if fassol < 1:
        print("Второй выйграл")
    print(fassol)


    # ХОД 2 ИГРОКА
    while True: # проверка корректности
        second = int(input("1, 2, 3 боба "))
        if second <= 3 and second >= 1:
            break
    beans(second)
    if fassol < 1:
        print("Первый выйграл")
        if fassol == 1:
            print("Первый победил")
        elif fassol == 1:
            print("Второй выйграл")
            break
        else:
            print(f"{fassol} фасоли")

    print(fassol)

import time
import random

print("Время проверить твою ловкость и "
      "скорость и понять, кто самый быстрый "
      "стрелок на западе! Когда увидишь 'СТРЕЛЯЙ',"
      "у тебя будет 0.3 секунды чтобы нажать Enter. Но если ты нажмёшь "
      "Enter раньше, то ты проиграл.")

input("Нажми Enter чтобы начать")
print("вермя пострелять")
time.sleep(random.randint(1, 5)) # случайное ожидание

start = time.time()
input("бум ")
end = time.time()
delta = end - start
print(f"{delta}сек")
if delta < 0.01: # Фальшстарт
    print("фальшстарт")

elif delta > 0.6:
    print("йу слоули мен")
else:
    print("гуд жоп мен")










def beans(x :int):  # отнимает фасоль
    global fassol
    fassol -= x



fassol = 20
while True:
    # ход 1-ого игрока
    while True  :  # Валидация(проверка корректности)
        first = int(input("1 игрок:1,2 или 3 боба из Южной Америки:"))
        if first <= 3 and first >= 1:
            break
    beans(first)
    if fassol < 1:
        print("Второй вин")
        break
    elif fassol == 1:
        print("Первый вин")
        break
    else:
        print(f"{fassol} фассоли")

    # ход 2-ого игрока
    while True  :  # Валидация(проверка корректности)
        second = int(input("2 игрок:1,2 или 3 боба из Южной Америки:"))
        if second <= 3 and second >= 1:
            break
    beans(second)
    if fassol < 1:
        print("Первый вин")
        break
    elif fassol == 1:
        print("Второй вин")
        break
    else:
        print(f"{fassol} фассоли")



import random
kolichestvo = int(input("напишите сколько костей бросаем:"))
slovar = {}
for i in range(kolichestvo, kolichestvo * 6 + 1):
    slovar[i] = 0

print(slovar)







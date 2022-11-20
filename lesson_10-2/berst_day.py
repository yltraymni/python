import random
import datetime

while True:
    number = input("Сколько дней рождения мы генерируем? (До 70) ")
    if not number.isdigit() or int(number) > 70 or int(number) < 2:
        print("Это по твоему смешно? Число от 2 до 70.")
        print("=" * 10)
    else:
        number = int(number)
        break

birthdays = []
startofyear = datetime.date(2022, 1, 1)
for _ in range(number):
    shiftofDays = datetime.timedelta(random.randint(0, 364)) # случайный сдвиг дней
    birthday = startofyear + shiftofDays
    birthdays.append(birthday)

for index in range(number):
    print(f"{index + 1}) {birthdays[index]}")

print("=" * 10)
for i in set(birthdays):    # set = множество, повторения исключены
    if birthdays.count(i) > 1:  # i встречается 2+ раза
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раза")

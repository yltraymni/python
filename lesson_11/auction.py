import os

total_bets = []
triger = "yes"
max_balanse = 100000
while triger == "yes":
    name = input("Ведите имя: ")
    bet = int(input("Ставка: "))
    temp_bet = {"name": name, "bet": bet}
    total_bets.append(temp_bet)
    triger = input("yes - продолжаем, no - останавливаем   ")
    os.system("cls||clear")

winner = {"name": " ", "bet": 0}
for i in range(len(total_bets)):
    if total_bets[i]["bet"] > winner["bet"]:
        winner["name"] = total_bets[i]["name"]
        winner["bet"] = total_bets[i]["bet"]

print(f"Победитель: {winner['name']}. Его ставка: {winner['bet']}")


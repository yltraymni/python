from pleer import MusicBox
pleer = MusicBox()
while True:
    pleer.play()
    guess = input("Что ты услышал? ")
    if guess == "":
        break

    pleer.check(guess)
print(f"У тебя {pleer.get_score()} очков")
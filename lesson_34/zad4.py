import random
from string import ascii_uppercase
stroka = ""
n = int(input())
for i in range(n):
    z = random.choice(ascii_uppercase)
    stroka += z
stroka = set(stroka)
print("".join(stroka))

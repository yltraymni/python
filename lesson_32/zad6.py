from string import ascii_lowercase
alphabet = ascii_lowercase
count = 0
a = input().lower()
b = input().lower()

for i in range(len(a)):
    if a[i] != b[i]:
        indx = alphabet.index(a[i])
        indx1 = alphabet.index(b[i])
        if indx > indx1:
            count = 1
        else:
            count = -1
        break
print(count)
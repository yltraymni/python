def abvgedeika(s):
    return s[::-1]
alpmax="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alpmini="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
reversebig=abvgedeika(alpmax)
reversemin=abvgedeika(alpmini)

sms=input("Введите " )
w = ''
for i in sms:
   if i not in alpmax or i not  in alpmini:
       w = w + i
       continue
   if i.isupper():
       ind=alpmax.index(i)
       letter=reversebig[ind]
   else:
       ind=alpmini.index(i)
       letter=reversemin[ind]
       w=w+letter
print(w)
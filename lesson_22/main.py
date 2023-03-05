# try:
#     number = int(input("Число: "))
#     print(10 / number)
# except ValueError:
#     print("Ы")
# except ZeroDivisionError:
#     print("Ы")
# else:  # не было исключений
#     print("Ы2")
# finally:  # Всегда
#     print(")))))")
import json

# JSON ЗАПИСЬ
# f = open("file.json", "w", encoding="utf-8")
# # f.write("true")
# peremennaya = [1, 2.3, [1, 4], (3, 5), None, True, "Stroka", "ENG", "РУС"]
# json.dump(peremennaya, f, ensure_ascii=False)
# f.close()
#
# # JSON ЧТЕНИЕ
# f = open("file.json", "r", encoding="utf-8")
# content = json.load(f)
# print(content)
# print(type(content))
# f.close()

# ЗАДАЧА 1
# sl = {}
# f = open("file.txt", "r", encoding="utf-8")
# f.close()
# u = f.readlines()
# for i in u:
#     dl = i.split(": ")
#     sl[dl[0]] = dl[1].rstrip()
# print(sl)
# x = open("file.json", "w",encoding="utf-8")
# json.dump(sl, x, ensure_ascii=False)
# x.close()

# ЗАДАЧА 2
# f = open("file.json", "r")
# sod = json.load(f)
# f.close()
# print(sod)
# for indx, elem in enumerate(sod):
#     if type(elem) == str:
#         sod[indx] += "!"
#     elif type(elem) in (int, float):
#         sod[indx] += 1
#     elif type(elem) == bool:
#         sod[indx] = not elem
#     elif type(elem) == list:
#         sod[indx] += elem
#     elif type(elem) == dict:
#         sod[indx]["newkey"] = None
# print(sod)


import requests
resp = requests.get(url="http://api.open-notify.org/iss-now.json").json()
print(resp["iss_position"])
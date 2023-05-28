slovar = {"key1": "value1",
          "key2": "value2",
          "key3": "value3",
          "key4": "value4",
          "key5": "value5"}
vall = []
keys = []
# keys = list(slovar.keys())
# val = list(slovar.values())
# print(keys, val)
for i in slovar:
    val1 = slovar[i]
    vall.append(val1)
    keys.append(i)
print(keys, vall)
import os
# СОЗДАНИЕ ПАПКИ
#os.mkdir(r"c:\Users\danil\desktop\test2")

# УДАЛЕНИЕ ПАПКИ
# os.rmdir("hello")
# os.rmdir(r"c:\Users\danil\desktop\somedir")


# ПЕРЕИМЕНОВАНИЕ ФАЙЛА

# os.rename(r"c:\Users\danil\desktop\test2\fgs.txt", r"c:\Users\danil\desktop\test2\GGRU.txt")
f = open("file.txt", "w")
x = input()
f.write(x)
f.close()

# os.mkdir(r"c:\Users\danil\desktop\file.txt")
os.remove(r"c:\Users\danil\desktop\dirtest\file.txt")
os.rmdir(r"c:\Users\danil\desktop\dirtest")
os.mkdir(r"c:\Users\danil\desktop\dirtest")
os.replace(r"C:\Users\danil\PycharmProjects\pythondfg\proekt\file.txt", r"c:\Users\danil\desktop\dirtest\file.txt")
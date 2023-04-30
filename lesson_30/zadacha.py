from random import randint
from tkinter import *
from tkinter import messagebox
# ЗАДАЧА 1

root = Tk()
root.geometry("500x500")

# label1 = Label(root, text="Логин:")
# label1.grid(column=0, row=0)
# label2 = Label(root, text="Пароль:")
# label2.grid(column=0, row=1)
#
# entry_log = Entry(root)
# entry_log.grid(column=1, row=0)
# entry_Pas = Entry(root, show="*")
# entry_Pas.grid(column=1, row=1,)
#
# btn = Button(root, text="кнопка")
# btn.grid(column=1, row=4, sticky=E)


# ЗАДАЧА 2
def fu(pelm):
    btn.place(x=randint(0,450), y=randint(0,450))

def win():
    messagebox.showinfo(message="Ты редан")

btn = Button(root, text="Нажми если редан!", command=win)
btn.place(x=0, y=0)
btn.bind("<Enter>", fu)








root.mainloop()
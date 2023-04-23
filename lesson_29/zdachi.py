from tkinter import *
# def button(event):
#     message = ent.get()
#     lab['text'] = message
#
#
# root = Tk()
# root.geometry("600x400")
# lab = Label(root, text="...")
# lab.pack()
#
# ent = Entry(root)
# ent.insert(0, "Впиши и ПКМ")
# ent.bind("<Button-3>", button)
# ent.pack()
#
#
# root.mainloop()


def get_rb():
    user_choose = rb_val.get()
    if user_choose == 1:
        lab["text"] = "Hallo" + rb["text"]
    else:
        lab["text"] = "Hallo " + rb1["text"]

win = Tk()
win.geometry("400x300")
lab = Label(win, text="Hallo")
lab.pack()

rb_val = IntVar()
rb = Radiobutton(win, text="World", variable=rb_val, value=1, command=get_rb)
rb.pack()


rb1 = Radiobutton(win, text="Python", variable=rb_val, value=2, command=get_rb)
rb1.pack()

win.mainloop()


# Задача 3
# def activation():
#     if cb_val.get() == True:
#         b["text"] = "Активна"
#         b["state"] = "normal"
#     else:
#         b["text"] = "Не активна"
#         b["state"] = "disabled"
#
#
# win = Tk()
# cb_val = BooleanVar()
# cb = Checkbutton(win, text="Активатор", variable=cb_val, onvalue=True,
#                  offvalue=False, command=activation)
# cb.pack()
#
# b = Button(win, text="Не активна", state="disabled")
# b.pack()
# win.mainloop()
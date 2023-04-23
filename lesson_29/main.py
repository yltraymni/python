from tkinter import *
win = Tk()
win.geometry("400x400")
win['bg'] = "pink"

# ======  ======== Надпись ========  =======
# lab = Label(win, text="Йоуу")  # создание
# lab.pack()  # размещение
# lab['bg'] = "black"
# lab['foreground'] = "green4"
# lab['fg'] = "green4"

# ======  ======= Однострочный ввод ========  =======
# ent = Entry(win,
#             width=15,
#             bor=10,
#             font="Arial 15, bold")
# ent.pack()

# =======  ======= Многострочный ввод ======= ========
# txt = Text(win, width=15, height=7, wrap='none')
# txt.pack()


# =======  ======= Кнопка ========  =========
# def action():
#     print("Принт")
#
# btn = Button(win, command=action)
# btn['text'] = "Нажми на меня"
# btn.pack()


# ======  ======== Checkbutton ======== ========
# def get_cb():
#     print(cb_val.get())
#
# cb_val = BooleanVar()
# cb = Checkbutton(win,
#                  text="Арсений баран",
#                  command=get_cb,
#                  variable=cb_val,  # привязываем к хранилищу
#                  onvalue=True,
#                  offvalue=False
#                  )
# cb.pack()
# cb.select()  # .select() - ставить галочку
# cb.deselect()  # .deselect() - убрать галочку


# =======  ======== Radiobutton ========  =======
# def get_rb():
#     print(rb_val.get())
#
# rb_val = IntVar()
# rb = Radiobutton(win,
#                  text="Арсений дурак",
#                  variable=rb_val,
#                  value=421,
#                  command=get_rb
#                  )
# rb.pack()
# rb2 = Radiobutton(win,
#                  text="Арсений тупица",
#                  variable=rb_val,
#                  value=23,
#                  command=get_rb
#                  )
# rb2.pack()


# ========  =========== Scale =========  ==========
def get_scala(val):
    print(scala.get())
# scala = Scale(win,
#               from_=50,
#               to=120,
#               orient=HORIZONTAL,
#               length=300,  # ДЛИННА ПОЛОСЫ
#               tickinterval=10,  # разметка
#               resolution=10,
#               command=get_scala)  # ШАГ
# scala.pack()


# =========  ========= Фотокарточка =========  ========
# img = PhotoImage(file="ghoul.png")
# lab_small = img.subsample(3, 3)  # .subsample() - уменьшение
# img_big = img.zoom(3, 3)
# img_poltora = img.subsample(3, 3).zoom(2, 2)
# lab = Label(win, image=img_poltora)
# lab.pack()


# =========  ========= Отступы ==========  ========
# Label(win, text='Чик пикс', bg="gold").pack()
# Label(win, text='Gик пикс', bg="gold").pack(pady=15, ipady=20)

win.mainloop()
from tkinter import *
root = Tk()
root.geometry("550x550")
c = Canvas(root, height=500, width=500, bg="wheat")
c.pack(anchor=CENTER, expand=True)

# ========== TEXT ============
# c.create_text(10, 10,
#               text="ХАйп",
#               anchor=NW,
#               font="Arial 50 bold",
#               fill='magenta')

# ========== RECTANGLE ===========
# c.create_rectangle(10, 10,
#                    150, 100,
#                    fill="green",
#                    outline='blue',
#                    width=12)


# ========== POLYGON ===========
#
# c.create_polygon(10, 10,
#                  150, 150,
#                  10, 150)

# ========== OVAL ===========
# c.create_oval(10, 10,
#               150, 200)

# ========== ARC ===========
# Сектор
# c.create_arc(10, 10,
#              150, 150,
#              extent=45,
#              start=45)

# Хорда
# c.create_arc(10, 10,
#              150, 150,
#              extent=500,
#              start=45,
#              style=CHORD)

# Дуга
# c.create_arc(10, 10,
#              150, 150,
#              extent=120,
#              start=45,
#              style=ARC,
#              outline="purple",
#              width=6)

# Отрисовка
# c.create_arc(10, 10,
#              150, 150,
#              extent=359,
#              start=45,
#              style=ARC,
#              outline="purple",
#              width=6,
#              dash="-. ",
#              activefill="pink",
#              activewidth=9)


# Event
# def nas(event):
#     print(event.x)
#
# btn = Button(root, text="Кнопка")
# btn.pack()
# btn.bind("<Button-3>", nas)






root.mainloop()

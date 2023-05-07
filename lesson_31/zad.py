from tkinter import *
root = Tk()
root.geometry("500x500")
c = Canvas(root, height=400, width=400, bg="wheat")
c.pack()
second = 0

# def seconds():
#     global second
#     c.delete("all")
#     second = second + 1
#     c.create_image(225, 215, image=img)
#     c.create_text(int(c["height"]) / 2, 450 / 2, text=second, font="Arial 50")
#     root.after(1000, seconds)
#     if second == 15:
#         root.destroy()
#
#
# c.create_text(int(c["height"]) / 2, 450 / 2, text=second, font="Arial 50")
# c.create_image(225, 215, image=img)
# root.after(1000, seconds)
# root.mainloop()


l = None
p = None

def lkm(event):
    global l
    l = (event.x, event.y)
    print(l)

def pkm(event):
    global p
    p = (event.x, event.y)
    print(p)

def stroitel():
    global l
    global p
    c.delete("all")
    if l and p:
        c.create_line(l[0], l[1], p[0], p[1])
        l, p = None, None

    else:
        print("потыкай в б")


btn = Button(root, text="Построить прямую", command=stroitel)
c.bind("<Button-1>", lkm)
c.bind("<Button-3>", pkm)

l = None
p = None
btn.pack()








root.mainloop()
























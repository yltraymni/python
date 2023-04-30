from tkinter import *
root = Tk()
root.geometry("500x500")




# Первый способ
# lst = ["Первый", "Второй", "Третий"]
# listbox = Listbox(root)
# listbox.pack()
#
# for elem in lst:
#     listbox.insert(END, elem)

# Второй способ
# lst = ["Первый", "Второй", "Третий"]
# lst_tk = StringVar(value=lst)  # получаем кортеж
# print(lst_tk.get())
# lstbox = Listbox(root, listvariable=lst_tk, selectmode=EXTENDED)
# lstbox.pack()
#
# def pech(pelmen):
#     for ind in lstbox.curselection():  # current = текущий
#         print(lst[ind])
#
#
# lstbox.bind('<<ListboxSelect>>', pech)

# btn = Button(root, text="Вывести", command=pech)
# btn.pack()


# =========== Messagebox ===========

# from tkinter import messagebox
# messagebox.showinfo("Лайк э босс", "Теперь знаешь")
# messagebox.showerror()
# messagebox.showwarning()


# ========== .pack() ==========
# btn = Button(root, text="Текст")
# btn.pack(anchor=SW, expand=True)
# btn.pack(fill=BOTH, expand=True)
# btn1 = Button(root, text="Текст")
# btn1.pack(pady=50)
# btn2 = Button(root, text="Текст")
# btn2.pack(pady=50)


# ====== .grid() ========
# столбик = column
# ряд = row
# btn = Button(root, text="Текст")
# btn.grid(column=0, row=0)
# btn1 = Button(root, text="Текст1")
# btn1.grid(column=1, row=0)
# btn2 = Button(root, text="Текст2")
# btn2.grid(column=2, row=0, rowspan=2, sticky=NS)
# btn3 = Button(root, text="Текст3")
# btn3.grid(column=0, row=1, columnspan=2, sticky=EW)


# ========= .place() ==========

# btn = Button(root, text="Текст")
# btn.place(x=10, y=10)


# ========= .after() ==========
# def fu():
#     print("Хайп")
#     root.after(1000, fu)
#
# root.after(3000, fu)


# ========= .bind() ==========
# def fu(pelm):
#     print("Хайп")
#
# btn1 = Button(root, text="Текст1")
# btn1.pack()
# btn1.bind("<Enter>", fu)  # при наведении мышкой
# btn1.bind("<MouseWheel>", fu)  # при кручении колесика мышки
# btn1.bind("<FocusIn>", fu)  # фокус(tab)
# btn1.focus_set()
# btn1.bind("<Return>", fu)  # enter
# btn1.bind("<h>", fu)  # h
# btn1.bind("<Shift-Up>", fu)  # Shift + Up


# ========= .set() ==========
# rb_val = IntVar()
# print(rb_val.get())
# rb_val.set(5)  # установить значение
# print(rb_val.get())


# ========= .show() ==========
# Entry(root, show="").pack()




# root.mainloop()


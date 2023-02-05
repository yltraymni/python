import easygui

# user_choose = easygui.msgbox(msg="hello world",
#                title="здравия желаю",
#                ok_button="стойку смирно принять",
#                image="img/apple.png")
#
# if user_choose == None:
#     easygui.msgbox(msg="ну и иди")
# elif user_choose == "стокуй смирно принять":
#     print("gg")


# easygui.buttonbox(
#     msg = "как дела",
#     title = "Вопрос",
#     choices=("Нормас", "плохо"),
#     images= ["img/boots.png", "img/ahganim.png"]
# )

# x = easygui.integerbox(
#       msg= "За сколько отдашь?",
#       upperbound = 150,
#       lowerbound = 50,
#       image = "img/boots.png",
#        default = 123
# )
# print(x)

pravda = easygui.enterbox(
    msg= "в доте есть натуралы",
    default="нет"
)
print(pravda)

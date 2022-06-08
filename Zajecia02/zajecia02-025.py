# =============================================
# M2Z25
import turtle as t
import Helpers as helpers

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Podaj ilość boków: ")
        numberSides, exitWhile = helpers.userVariableINT(userVar)
        if numberSides <= 2:
            print("Musisz podać co najmniej 3 boki ;)")
            exitWhile = False
    exitWhile = False
    while not exitWhile:
        userVar = input("Podaj długość boku: ")
        lenghtSides, exitWhile = helpers.userVariableINT(userVar)
        if lenghtSides < 1:
            print("Musisz podaj co najmniej wartość 1")

    t.penup()
    t.goto(-lenghtSides * 1.5, lenghtSides * 1.5)
    t.pendown()

    for i in range(0, numberSides):
        t.forward(lenghtSides)
        t.right(360 / numberSides)

    t.Screen().exitonclick()

    helpers.exitProgram()
    exitWhile = False

# =============================================
# =============================================
# M2Z24
import turtle as t
import Helpers as helpers


def drawFlag(variable):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(variable)
    t.forward(200)
    for i in range(0, 3):
        t.left(90)
        t.forward(30)
    t.left(90)


exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Podaj ilość chorągiewiek: ")
        numberFlags, exitWhile = helpers.userVariableINT(userVar)
    arroundFlags = 360 / numberFlags

    for i in range(0, numberFlags):
        drawFlag(arroundFlags)

    t.Screen().exitonclick()

    helpers.exitProgram()
    exitWhile = False

# =============================================

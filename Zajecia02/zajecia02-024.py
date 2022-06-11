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


while True:
    print("################################################################################\n")
    numberFlags = helpers.userVariableIntNEW("Podaj ilość chorągiewiek: ")
    arroundFlags = 360 / numberFlags

    for i in range(0, numberFlags):
        drawFlag(arroundFlags)

    t.Screen().exitonclick()

    helpers.exitProgram()

# =============================================

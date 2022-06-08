# =============================================
# M2Z21
import turtle as t
import Helpers as helpers

exitWhile = False
while not exitWhile:
    print("################################################################################\n")
    while not exitWhile:
        userVar = input("Podaj promień okręgów: ")
        radius, exitWhile = helpers.userVariableINT(userVar)
    exitWhile = False
    while not exitWhile:
        userVar = input("Podaj ilość okręgów: ")
        numberCircles, exitWhile = helpers.userVariableINT(userVar)
    exitWhile = False
    while not exitWhile:
        userVar = input("Podaj odstęp między okręgami: ")
        spaceBetween, exitWhile = helpers.userVariableINT(userVar)

    t.speed(1000)
    t.penup()
    t.goto(-50, 50)
    for i in range(0, numberCircles):
        t.pendown()
        t.circle(radius)
        t.penup()
        t.forward(spaceBetween)
        t.right(22)

    t.Screen().exitonclick()

    helpers.exitProgram()
    exitWhile = False

# =============================================
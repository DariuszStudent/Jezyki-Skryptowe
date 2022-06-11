# =============================================
# M2Z22
import turtle as t
import Helpers as helpers

while True:
    print("################################################################################\n")
    numberCircles = helpers.userVariableIntNEW("Podaj ilość okręgów: ")
    spaceBetween = helpers.userVariableIntNEW("Podaj o ile promień ma być większy od poprzedniego: ")

    radius = 20
    t.penup()
    t.left(90)
    t.goto(0 - spaceBetween, 0)
    for i in range(0, numberCircles):
        t.penup()
        t.goto(0 + spaceBetween, 0)
        t.pendown()
        t.circle(radius)
        radius += spaceBetween

    t.Screen().exitonclick()

    helpers.exitProgram()

# =============================================
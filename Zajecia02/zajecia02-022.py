# =============================================
# M2Z22
import turtle as t
import Helpers as helpers

while True:
    print("################################################################################\n")
    numberCircles = helpers.userVariableINTstring("Podaj ilość okręgów: ")
    spaceBetween = helpers.userVariableINTstring("Podaj o ile promień ma być większy od poprzedniego: ")
    helpers.turtleXY(200)
    goLeft = 0

    radius = 20
    t.penup()
    t.goto(-20, 0)
    t.right(90)
    for i in range(0, numberCircles):
        t.pendown()
        t.circle(radius)
        t.penup()
        goLeft -= spaceBetween
        t.goto(goLeft - 20, 0)
        radius += spaceBetween

    t.Screen().exitonclick()

    helpers.exitProgram()

# =============================================

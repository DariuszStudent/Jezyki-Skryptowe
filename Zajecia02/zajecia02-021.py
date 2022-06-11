# =============================================
# M2Z21
import turtle as t
import Helpers as helpers

while True:
    print("################################################################################\n")
    radius = helpers.userVariableIntNEW("Podaj promień okręgów: ")
    numberCircles = helpers.userVariableIntNEW("Podaj ilość okręgów: ")
    spaceBetween = helpers.userVariableIntNEW("Podaj odstęp między okręgami: ")

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

# =============================================
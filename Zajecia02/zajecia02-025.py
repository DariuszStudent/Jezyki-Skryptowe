# =============================================
# M2Z25
import turtle as t
import Helpers as helpers

while True:
    print("################################################################################\n")
    numberSides = helpers.userVariableINTstring("Podaj ilość boków: ")
    if numberSides <= 2:
        print("Musisz podać co najmniej 3 boki ;)")
        continue
    lenghtSides = helpers.userVariableINTstring("Podaj długość boku: ")
    while True:
        if lenghtSides < 1:
            print("Musisz podaj co najmniej wartość 1")
        else:
            break

    t.penup()
    t.goto(-lenghtSides * 1.5, lenghtSides * 1.5)
    t.pendown()

    for i in range(0, numberSides):
        t.forward(lenghtSides)
        t.right(360 / numberSides)

    t.Screen().exitonclick()

    helpers.exitProgram()

# =============================================
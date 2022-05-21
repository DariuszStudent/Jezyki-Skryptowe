# =============================================
# M2Z23
import turtle
turtl = turtle.Screen()

t = turtle.Turtle()
promien = 55
ile = 6
skok = 360 / ile
odstep = 15

t.speed(10)
t.goto(0, 0)
t.pendown()
for i in range(0, ile):
    t.penup()
    t.left(skok)
    t.forward(odstep)
    t.pendown()
    t.circle(promien)
turtle.Screen().exitonclick()

# =============================================
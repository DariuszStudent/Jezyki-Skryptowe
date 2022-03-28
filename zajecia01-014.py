# =============================================
# M1Z14
import turtle

t = turtle.Turtle()

t.penup()
t.goto(-300, 0)
t.pendown()
for i in range(0, 11):
    t.forward(50)
    t.dot(5)
t.forward(50)
t.penup()
t.goto(0, 300)
t.right(90)
t.pendown()
for i in range(0, 11):
    t.forward(50)
    t.dot(5)
t.forward(50)
t.penup()
t.goto(50, 150)
t.pendown()
for i in range(0, 4):
    t.forward(50)
    t.left(90)
t.penup()
t.left(90)
t.goto(-200, -50)
t.pendown()
for i in range(0, 360):
    t.forward(1)
    t.right(1)
t.penup()
t.goto(0, 0)


# =============================================

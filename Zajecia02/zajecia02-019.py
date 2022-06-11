# =============================================
# M2Z19
import turtle as t

t.penup()
t.goto(-50, 50)
t.pendown()
for i in range(0, 4):
    t.forward(100)
    t.right(90)
t.delay(200)
t.clear()
t.penup()
t.goto(-22, 22)
t.pendown()
for i in range(0, 8):
    t.forward(30)
    t.right(45)

t.Screen().exitonclick()

# =============================================
import turtle

scr = turtle.Screen()
t = turtle.Turtle()
t.speed(8)

DIMX = 300
DIMY= 400
XSTART = DIMX / 2
YSTART= DIMY / 2
rozm_czcionki = 15
skala = 1.35

dane = {
'p1':(0,0),
'p2':(-10,-5),
'p3':(11,7),
'p4':(-40,-60),
}

dane2 = {
0:(0,0,'Alnilan'),
1:(21,12,'Mintka'),
2:(59,90,'Meisa'),
3:(65,-41,'Rigel'),
4:(-20,-15,'Alnitk'),
5:(-73,82,'Betelguse'),
6:(-50,-70,'Saiph'),
}

scr.setup(DIMX, DIMY)
scr.bgcolor("black")
t.pencolor("white")
t.penup()
t.hideturtle()

t.penup()
t.goto(-DIMX/2+10, DIMY/2-(rozm_czcionki*2))

t.color("white")
style = ("Arial", 15, "italic")
t.write("Gwiadozbior Oriona", font=style,align='left')
t.penup()

for e in dane2:
    t.goto(dane2[e][0]*skala,dane2[e][1]*skala)
    t.dot()
    t.penup()
    t.forward(15)
    t.penup()
    t.write(dane2[e][2], font='Arial', align='left')
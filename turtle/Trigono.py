import turtle as tur
import math as mt

tur.speed(0)
# screen.bgcolor('blue')
tur.pensize(1)

def axis():
    tur.pencolor('green')
    # X axis 
    tur.penup()
    tur.goto(-200, 0)
    tur.pendown()
    tur.goto(200, 0)

    # Y axis
    tur.penup()
    tur.goto(0, -200)
    tur.pendown()
    tur.goto(0, 200)



axis()
tur.home()
tur.pencolor('red')


tur.forward(50)

tur.hideturtle()
tur.forward(50)
# tur.showturtle()
# tur.isvisible()

# Gelombang
# tur.penup()
# for i in range (-300,300,6):
#     y = (mt.sin(i))* (2*mt.pi*20)
#     tur.goto(i,y)
#     tur.pendown()


tur.done()
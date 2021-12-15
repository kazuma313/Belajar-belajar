import turtle as tur
from turtle import Screen, Shape, Turtle

screen = tur.Screen()
screen.bgcolor('SkyBlue')
# tur.color('blue', 'red')
# tur.begin_fill()

shape = Shape('compound')
# turtle = Turtle(visible=True)
# tur.penup()
tur.begin_poly()
# while True:
#     tur.forward(100)
#     tur.left(90)
#     if abs(tur.pos()) < 1:
#         break

tur.forward(100)
tur.left(90)
tur.forward(100)

tur.end_poly()
shape.addcomponent(tur.get_poly(), 'red')

screen.register_shape('kotak', shape)

# tur.end_fill()
# tur.reset()

tur.shape('kotak')
tur.penup()
tur.goto(50, 50)
screen.mainloop()
# tur.done()

import turtle
import random
zul = turtle.Turtle()
zul.speed(0)
zul.width(10)

colors = ['red', 'blue', 'green', 'purple', 'white', 'black']


def up():
    zul.setheading(90)
    zul.forward(100)


def left():
    zul.setheading(180)
    zul.forward(100)


def right():
    zul.setheading(0)
    zul.forward(100)


def down():
    zul.setheading(270)
    zul.forward(100)


def clickleft(x, y):
    zul.color(random.choice(colors))


def clickright(x, y):
    zul.stamp()


turtle.listen()

turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(right, 'Right')
turtle.onkey(left, 'Left')

turtle.mainloop()

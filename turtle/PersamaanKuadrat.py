import turtle as tur
import math

screen = tur.Screen()

tur.speed(0)
# screen.bgcolor('blue')
tur.pensize(1)

class Garis:
    def __init__(self, batas1, batas2):
        self.batas1 = batas1
        self.batas2 = batas2

    def axis(self):
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
        tur.home()




    def persamaanKudrt(self, a, b, c):
        tur.pencolor('red')

        tur.penup()
        for x in range (self.batas1, self.batas2):
            
            
            

            # y = ax^2 + bx + c
            y = (a * (x ** 2)) + (b * x) + c

            # y = 4 - x^2
            # y = 4 - (x**2)



            tur.goto( x, y )
            tur.pendown()

    def parabola(self, a):
        tur.pencolor('blue')

        tur.penup()

        for x in range (self.batas1, self.batas2):

            # parabola => y = ax^2
            y = (a * x) ** 2
            tur.goto( x, y )
            tur.pendown()


garis = Garis(-20, 20)
garis.axis()
garis.persamaanKudrt(-1,20,-50)
garis.parabola(1)


tur.done()
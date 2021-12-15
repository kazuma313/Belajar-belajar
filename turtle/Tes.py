#Graphing Algorithm - www.101computing.net/graphing-algorithm
import turtle
import math

myPen = turtle.Turtle()
myPen.speed(0)

screen = turtle.Screen()
screen.bgcolor("#000000")

#A procedure to draw both the X and Y axis on screen
def drawAxis():
  # X Axis
  myPen.penup()
  myPen.goto(-200,0)
  myPen.pendown()
  myPen.goto(200,0)
  # Y Axis
  myPen.penup()
  myPen.goto(0,-200)
  myPen.pendown()
  myPen.goto(0,200)
  
#A procedure to trace a line: y = a * x + b
def drawLine(a, b, c):
  myPen.penup()
  for x in range(-200,201):
    y = (a * x) ** 2 + b * x + c
    myPen.goto(x,y)
    myPen.pendown()
  
  myPen.penup()
  myPen.goto(-180,180)
  #Work out and display the mathematical equation
  equation = ""
  if a==0:
    equation = " y = " + str(b)
  else:
    if b>0:
      equation = " y = " + str(a) + "x + " + str(b) 
    elif b<0:
      equation = " y = " + str(a) + "x " + str(b) 
    else:
      equation = " y = " + str(a)

  myPen.write(equation, None, "14pt bold")

# Main Program Starts Here
myPen.color("white")
drawAxis()
myPen.pensize(2)
myPen.color("#FF59F7")
drawLine(-1, 0, 100)

screen.tracer(0)
from turtle import *

import turtle as tp

# color('red', 'yellow')
# begin_fill()
speed('fast')

shape = tp.Shape('compound')

width(10)
begin_poly()
batas = 0

while True:
    forward(200)
    print(pos())
    left(72)
    batas += 1
    if batas == 5:
        batas = 0
        break

end_poly()
shape.addcomponent(get_poly(), 'red')


begin_poly()
while True:
    forward(200)
    print(pos())
    left(120)
    batas += 1
    if batas == 5:
        batas = 5
        break

end_poly

shape.addcomponent(get_poly(), 'blue')
tp.register_shape('tempat', shape)
# tp.reset()
tp.shape('tempat')
setpos(0, 0)
setheading(90)

# end_fill()
done()

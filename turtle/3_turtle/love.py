import math as mt
import turtle as tur


tur.speed('fast')


def curve():
    for i in range(200):

        # Defining step by step curve motion
        tur.right(1)
        tur.forward(1)


Kiri = tur.Shape('compound')
Kanan = tur.Shape('compound')

tur.begin_poly()
tur.left(140)
tur.forward(113)
curve()
tur.end_poly()
Kiri.addcomponent(tur.get_poly(), 'red')
tur.register_shape('kiri', Kiri)


tur.begin_poly()
tur.left(120)
curve()
tur.forward(112)
tur.end_poly()
Kanan.addcomponent(tur.get_poly(), 'blue')
tur.register_shape('kanan', Kanan)


tur.shape('kiri')
tur.setpos(90, -90)
tur.shape('kanan')
tur.setpos(-90, 90)

tur.done()

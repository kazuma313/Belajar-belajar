import math


def segitiga_kiri(batas):
    for i in range(batas):
        print("")
        for j in range(i):
            print('*', end='')


def segitiga_kanan(batas):
    for i in range(batas, 0, -1):
        print('')
        for j in range(i):
            print("*", end='')


def kotak():
    for i in range(10):
        print('')
        for j in range(10):
            print('*', end='')


for i in range(2):
    print()
    for p in range(1):
        print(' ', end='')
    for j in range(2, i, -1):
        print(' ', end='')
    for k in range(i+1):
        print("*", end='')
    for m in range(i):
        print("*", end='')

print()
for j in range(7):
    print('*', end='')


for i in range(2):
    print("")
    for j in range(i+1):
        print(' ', end='')
    for k in range(2, i, -1):
        print('*', end='')
    for m in range(1):
        print('*', end='')
    for n in range(2, i, -1):
        print('*', end='')

for i in range(2):
    print()
    for p in range(1):
        print(' ', end='')
    for j in range(2, i, -1):
        print('*', end='')
    for k in range(i+1):
        print(" ", end='')
    for m in range(i):
        print(" ", end='')
    for n in range(2, i, -1):
        print('*', end='')

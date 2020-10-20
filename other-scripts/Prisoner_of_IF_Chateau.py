#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Over the years of his imprisonment, the prisoner of the IF castle made a rectangular hole in the wall
   measuring D × E. The castle is built of bricks, with the size: A × B × C. The program determines if the prisoner
   can throw bricks into the sea through this hole (obviously, the sides of the brick assumed to be parallel to the sides of the hole)."""


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a >= b and b >= c:
    if (d >= a and e >= b) or (d >= b and e >= a):
        print('YES')
    elif (d >= b and e >= c) or (d >= c and e >= b):
        print('YES')
    else:
        print('NO')
elif b >= a and a >= c:
    if (d >= b and e >= a) or (d >= a and e >= b):
        print('YES')
    elif (d >= a and e >= c) or (d >= c and e >= a):
        print('YES')
    else:
        print('NO')
elif c >= a and a >= b:
    if (d >= c and e >= a) or (d >= a and e >= c):
        pint('YES')
    elif (d >= a and e >= b) or (d >= b and e >= a):
        print('YES')
    else:
        print('NO')
elif b >= c and c >= a:
    if (d >= b and e >= c) or (d >= c and e >= b):
        pint('YES')
    elif (d >= c and e >= a) or (d >= a and e >= c):
        print('YES')
    else:
        print('NO')
elif a >= c and c >= b:
    if (d >= a and e >= c) or (d >= c and e >= a):
        pint('YES')
    elif (d >= c and e >= b) or (d >= b and e >= c):
        print('YES')
    else:
        print('NO')
elif c >= b and b >= a:
    if (d >= c and e >= b) or (d >= b and e >= c):
        pint('YES')
    elif (d >= b and e >= a) or (d >= a and e >= b):
        print('YES')
    else:
        print('NO')

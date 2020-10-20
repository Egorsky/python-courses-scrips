#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Given the coordinates of two points on the plane, 
   it is required to determine whether they lie in the same coordinate quarter
   or not (all coordinates are nonzero). 4 numbers are entered into the program:
   the coordinates of the first point (x1, y1) and the coordinates of the second point (x2, y2)."""


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 >= 0 and x2 >= 0 and y1 >= 0 and y2 >= 0:
    print('YES')
elif x1 <= 0 and x2 <= 0 and y1 >= 0 and y2 >= 0:
    print('YES')
elif x1 >= 0 and x2 >= 0 and y1 <= 0 and y2 <= 0:
    print('YES')
elif x1 <= 0 and x2 <= 0 and y1 <= 0 and y2 <= 0:
    print('YES')
else:
    print('NO')

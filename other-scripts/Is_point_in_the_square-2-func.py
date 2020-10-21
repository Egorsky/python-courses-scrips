#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters two real numbers x and y. Check if the point with coordinates (x, y)
   belongs to the shaded square (including its border). If the point belongs to 
   the rhombus side of which is equal to the square root of 2 and center in (0, 0) point, 
   output word YES, otherwise print the word NO."""


def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1

x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')

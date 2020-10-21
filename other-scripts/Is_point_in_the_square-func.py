#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters real numbers x and y. The program will check
   if the point with coordinates (x, y) belongs to a square 
   with sides of 2 units and the middle at the center of the origin. 
   If the point belongs to the square, the word YES is displayed, otherwise the word NO."""


def IsPointInSquare(x, y):
    return ((-1 <= x <= 1) and (-1 <= y <= 1))


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')

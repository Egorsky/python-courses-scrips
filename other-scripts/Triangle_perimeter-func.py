#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A function is written that calculates
   the perimeter of a triangle by the coordinates of its three vertices.
   The input to the program is 6 integers - coordinates x₁, y₁, x₂, y₂, x₃, y₃ 
   of the triangle vertices. All numbers do not exceed 30,000 in absolute value."""


from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
dist1 = sqrt((x2 - x1)**2 + (y2 - y1)**2)  # a distance between 1st point and 2nd one
dist2 = sqrt((x2 - x3)**2 + (y2 - y3)**2)
dist3 = sqrt((x3 - x1)**2 + (y3 - y1)**2)
per = dist1 + dist2 + dist3
print(per)

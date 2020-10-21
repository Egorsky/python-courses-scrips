#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""You are given real coefficients a, b, c, with a != 0.
   The program solves the quadratic equation ax² + bx + c = 0 and displays all its roots."""


from math import sqrt

a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
if d == 0:
    x = (-b + sqrt(d)) / (2 * a)
    print(x)
elif d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    if x1 < x2:
        print(x1, x2)
    elif x1 > x2:
        print(x2, x1)

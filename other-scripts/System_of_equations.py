#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User enters real numbers a, b, c, d, e, f the coefficients of the equations of the system"""
"""It is known that the system of linear equations:
  ax + by = e
  cx + dy = f
  has exactly one solution. The program outputs two numbers x and y, which are the solution to this system."""

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == 0:
    y = e / b
    x = (f - d * y) / c
else:
    y = (a * f - e * c) / (a * d - b * c)
    x = (e - b * y) / a
print(x, y)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The lengths of the sides of the triangle are given.
   The program calculates the area of the triangle. 
   The calculation uses Heron's formula."""


a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) * (1 / 2)  # half-perimeter
s = (p * (p - a) * (p - b) * (p - c))**0.5  # Heron's formula

print('{0:.6f}'.format(s))

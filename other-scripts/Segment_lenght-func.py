#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters four real numbers: x₁, y₁, x₂, y₂. 
   The distance (x1, y1, x2, y2) function has been written,
   which calculates the distance between the points (x₁, y₁) and (x₂, y₂)."""


from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
dist1 = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(dist1)

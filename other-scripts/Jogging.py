#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""For a given number N, 
   print all integer powers of two
   not exceeding N in ascending order."""


x = int(input())  # the first day
y = int(input())  # the amount of kilometers
k = 1
while x < y:
    x = x + 0.1 * x
    k = k + 1
print(k)

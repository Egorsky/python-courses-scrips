#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Two integers A and B are entered. 
   The program outputs all numbers from A to B inclusive, 
   in ascending order if A <B, or in descending order otherwise."""


a = int(input())
b = int(input())

if a < b:
    for i in range(a, b + 1, 1):
        print(i, end=' ')
elif a > b:
    for j in range(a, b - 1, -1):
        print(j, end=' ')
elif a == b:
    print(a)

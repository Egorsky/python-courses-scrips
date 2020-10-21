#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Several numbers are entered. 
   The program calculates how many of them are equal to zero and outputs this number."""


n = int(input())
zeros = 0
for i in range(1, n + 1):
    i = int(input())
    if i == 0:
        zeros += 1
print(zeros)

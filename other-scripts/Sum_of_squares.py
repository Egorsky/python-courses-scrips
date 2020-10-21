#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters the number n
   the program calculates the sum 1² + 2² + 3² + ... + n²."""

n = int(input())
sumz = 0
for i in range(1, n + 1):
    i = i**2
    sumz += i
print(sumz)

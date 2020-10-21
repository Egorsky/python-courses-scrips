#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""For a given number N, 
   print all integer powers of two
   not exceeding N in ascending order."""


n = int(input())
i = 0
while i**2 < n:
    i = i + 1
    if i**2 > n:
        break
    print(i**2)

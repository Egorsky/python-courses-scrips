#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The chocolate has the form of a rectangle divided into n × m slices.
   The chocolate can be broken into two parts once in a straight line. 
   The program determines whether it is possible to break off a part of 
   the chocolate bar, consisting of exactly k slices."""


n = int(input())
m = int(input())
k = int(input())
d = m * n
if (k % n == 0 or k % m == 0) and k < d:
    print('YES')
else:
    print('NO')

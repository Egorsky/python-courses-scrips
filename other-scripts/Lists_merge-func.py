#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters two integer lists A and B,
   sorted in non-decreasing order. 
   The program concatenates them into one ordered list C 
   (contains len (A) + len (B) elements)."""


def merge(a, b):
    c = a + b
    c.sort()
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*merge(a, b))

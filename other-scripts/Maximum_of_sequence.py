#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The sequence consists of integers
   and ends with the number 0. 
   The program determines the value
   of the largest element of the sequence."""


now = int(input())
maxNum = now
while now != 0:
    now = int(input())
    if now == 0:
        break
    if now > maxNum:
        maxNum = now
print(maxNum)

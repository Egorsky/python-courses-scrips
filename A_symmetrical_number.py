#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters a four-digit number. The program determines if its decimal notation is symmetric.
   If the number is symmetric, then 1 is displayed, otherwise another integer is displayed. 
   The number can have less than four digits, then you need to consider that its decimal notation is padded on the left with zeros."""

var = int(input())
right = var % 100
right_fx1 = str(str(right % 10) + str(right // 10))
right_fx2 = int(right_fx1)
left = var // 100
print(left - right_fx2 + 1)

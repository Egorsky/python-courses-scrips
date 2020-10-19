#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The program reads two integers A and B and outputs the largest of them.
   The numbers are integers from 1 to 1000. No functions, branches or loops were used."""


a = int(input())
b = int(input())
max1 = (a // b)  # returns 0 or 1
max2 = (b // a)
max3 = (max1 * a + max2 * b) // (max1 + max2)
print(max3)

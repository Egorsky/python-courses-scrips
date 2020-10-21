#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The price of the product is indicated in dollars
   with an accuracy of cents, that is, a real number
   with two digits after the decimal point. 
   The program outputs two integer variables, 
   the cost of a product, as an integer number of dollars and
   an integer number of cents. 
   The task is solved without special conditional statements and loops on purpose."""


c = float(input())
b = '{0:.2f}'. format(float(c) - int(c))
d = round(float(b) * 100)
print(int(c), d)

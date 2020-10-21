#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The interest rate on the deposit is P percent per annum,
   which is added to the deposit amount. The contribution is X dollars Y cents.
   The program determines the size of the contribution in a year.
   When solving the problem, conditional instructions and loops were not used on purpose."""


p = int(input())
x = int(input())
y = int(input())
y1 = float(y / 100.0001)
p1 = float(p / 100)
rate = (x + y1) + ((x + y1)*p1)
rate_dol = int(rate)
rate_cen = round(float(('{0:.2f}'. format(float(rate) - int(rate))))*100)
print(int(rate_dol), int(rate_cen)

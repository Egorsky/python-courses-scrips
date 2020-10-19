#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User enter the amount of minutes that passed from the midnight
   (<10**7). Program shows amount of hours 0 - 23 and minutes 0 59"""



clck = int(input())
op1 = clck // 60 % 24  # amount of hours
op2 = clck % 60  # amount of minutes
print(op1, op2)

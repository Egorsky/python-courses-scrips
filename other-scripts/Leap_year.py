#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A natural number is given. The program determines if the year with
   the given number is a leap year. If the year is a leap year, 
   it outputs YES, otherwise it outputs NO. Recall that, 
   according to the Gregorian calendar, a year is a leap year
   if its number is a multiple of 4, but not a multiple of 100,
   or if it is a multiple of 400."""

year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print('YES')
elif year % 400 == 0:
    print('YES')
else:
    print('NO')

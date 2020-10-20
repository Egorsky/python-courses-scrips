#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters the number of seconds since the beginning of the day, 
   and the clock displays it in the format h:mm:ss. First digit represents
   the amount of hours (0 - 23) then minutes and then seconds."""


sec = int(input())  # the user enters the amount of seconds
h1 = sec // 3600 % 24  # counting the hours
m1 = sec % 3600 // 60 // 10  # counting the first digit for minutes
m2 = sec % 3600 // 60 % 10  # counting the second digit for minutes
s1 = sec % 3600 % 60 // 10  # counting the first digit for seconds
s2 = sec % 3600 % 60 % 10  # counting the second digit for seconds
print(h1, ":", m1, m2, ':', s1, s2, sep='')

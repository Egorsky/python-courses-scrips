#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters a string. If the letter f occurs only once in this line,
   the program prints its index. If it occurs two or more times, the program displays
   the index of its first and last occurrence. If the letter f does not appear in the given line,
   the program does not output anything. 
   The count method and loops to solve this problem were not used on purpose."""


string = input()
p = string.find('f')
s = string.rfind('f')
if p != s:
    print(p, s)
elif p == s and p > 0:
    print(p)

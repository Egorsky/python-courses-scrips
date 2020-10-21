#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters a string of words separated by spaces. 
   The program determines how many words it contains."""


s = input()
b = s.count(' ')
count = b + 1
if s[-1] == ' ':
    count -= 1
print(count)

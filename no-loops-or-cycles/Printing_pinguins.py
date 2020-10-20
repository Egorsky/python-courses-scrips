#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User enters a number 1 through 9 and program prints that number of
   pinguins"""

data = int(input())
a = '   _~_    '
b = '  (o o)   '
c = ' /  V  \  '
d = '/(  _  )\ '
e = '  ^^ ^^   '
print(a * data, b * data, c * data, d * data, e * data, sep='\n')

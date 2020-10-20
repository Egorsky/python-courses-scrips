#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The chocolate has the form of a rectangle divided into n × m slices.
   The chocolate can be broken into two parts once in a straight line. 
   The program determines whether it is possible to break off a part of 
   the chocolate bar, consisting of exactly k slices."""


a = int(input())
b = int(input())
c = int(input())
if a == b < c or a == c < b or b == c < a:
    print('impossible')
elif a > 0 and b > 0 and c > 0:
        if (a + b) > c or (b + c) > a or (a + c) > b:
            if (a + b) != c or (b + c) != a or (a + c) != b:
                if a > b and a > c:
                    if a**2 == b**2 + c**2:
                        print('rectangular')
                    elif a**2 > b**2 + c**2:
                        print('obtuse')
                    elif a**2 < b**2 + c**2:
                        print('acute')
                elif b > a and b > c:
                    if b**2 == a**2 + c**2:
                        print('rectangular')
                    elif b**2 > a**2 + c**2:
                        print('obtuse')
                    elif b**2 < a**2 + c**2:
                        print('acute')
                    else:
                        print('impossible')
                elif c > a and c > b:
                    if c**2 == b**2 + a**2:
                        print('rectangular')
                    elif c**2 > b**2 + a**2:
                        print('obtuse')
                    elif c**2 < b**2 + a**2:
                        print('acute')
else:
    print('impossible')

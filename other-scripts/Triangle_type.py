#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Given three sides of a triangle a, b, c. 
   The program determines the type of a triangle with given sides
   and outputs one of four words: "rectangular" for a right-angled triangle,
   "acute", "obtuse", or "impossible" if a triangle with such sides does not exist
   (degenerate triangle is also impossible)."""


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

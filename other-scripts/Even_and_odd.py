#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Given three integers A, B, C. 
   The program determines whether 
   there is at least one even and at least one odd among them."""


a = int(input())
b = int(input())
c = int(input())
if a % 2 != 0 and b % 2 == 0 and c % 2 != 0:
    print('YES')
elif a % 2 == 0 and b % 2 == 0 and c % 2 != 0:
    print('YES')
elif a % 2 == 0 and b % 2 != 0 and c % 2 != 0:
    print('YES')
elif a % 2 != 0 and b % 2 != 0 and c % 2 == 0:
    print('YES')
elif a % 2 != 0 and b % 2 == 0 and c % 2 == 0:
    print('YES')
elif a % 2 == 0 and b % 2 != 0 and c % 2 == 0:
    print('YES')
else:
    print('NO')

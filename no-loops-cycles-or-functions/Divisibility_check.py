#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The program checks if the number A is evenly divisible by the number B."""


a = int(input())
b = int(input())
yes = a % b  # a first check, returns 1 or 0
f = 0**yes  # using this for the upcoming check. 0**0 = 1
print(('Yes' * f) + ('No' * (1 - f)))  # because of upper circumstances, only one part of the string can be printed

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The input is a sequence of natural numbers of length n≤1000.
   The program counts the product of the fifth powers of the numbers in the sequence."""


import functools

print(functools.reduce(
    lambda x, y: x * y,
    map(
        int, input().split()
    )
)**5
     )

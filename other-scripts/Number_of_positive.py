#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The program prints the amount of positive elements in the input list."""


a = list(map(int, input().split()))
count = 0
for i in a:
    if i > 0:
        count += 1
print(count)

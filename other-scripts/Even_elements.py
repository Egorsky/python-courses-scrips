#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The program prints even elements only."""


a = list(map(int, input().split()))
newlist = []
for i in a:
    if i % 2 == 0:
        newlist.append(i)
print(' '.join(map(str, newlist)))

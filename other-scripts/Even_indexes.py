#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The program displays all the elements of the input 
   list with even indices (that is, A [0], A [2], A [4], ...)."""


def altElement(a):
    return a[::2]


a = list(map(int, input().split()))

print(' '.join(map(str, altElement(a))))

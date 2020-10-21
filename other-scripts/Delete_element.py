#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters a sequence of numbers and the index of an item in the list k. 
   The program removes the element with index k from the list, shifting all elements
   to the right of the element with index k to the left."""


a = list(map(int, input().split()))
k = int(input())
a.pop(k)
print(' '.join(map(str, a)))

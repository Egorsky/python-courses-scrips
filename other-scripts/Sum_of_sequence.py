#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The program determines the sum of
   all elements of the sequence ending with the number 0."""


sumSeq = 0
now = int(input())
while now != 0:
    sumSeq = sumSeq + now
    now = int(input())
print(sumSeq)

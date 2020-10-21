#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The user enters a sequence of numbers,
   where all elements are pairwise distinct.
   The program swaps the minimum and maximum elements of this list."""


a = list(map(int, input().split()))
ind_max = a.index(max(a))
ind_min = a.index(min(a))
a[ind_max], a[ind_min] = a[ind_min], a[ind_max]

print(*a)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The chess king moves horizontally, vertically and diagonally, 
   but only 1 square. Given two different squares of the chessboard 
   (with coordinates h_1, v_1, h_2, v_2), the program determines whether
   the king can get from the first square to the second in one move."""


h_1 = int(input())  # horizontal basic coordinate
v_1 = int(input())  # vertical basic coordinate
h_2 = int(input())  # horizontal target coordinate
v_2 = int(input())  # vertical target coordinate

"""Program goes through all possible cases that can appear."""

if v_1 == v_2 and h_1 == h_2:
    print('YES')
elif h_2 == h_1 + 1 and v_2 == v_1:
    print('YES')
elif h_2 == h_1 - 1 and v_2 == v_1:
    print('YES')
elif v_2 == v_1 + 1 and h_2 == h_1:
    print('YES')
elif v_2 == v_1 - 1 and h_2 == h_1:
    print('YES')
elif v_2 == v_1 + 1 and h_2 == h_1 + 1:
    print('YES')
elif v_2 == v_1 - 1 and h_2 == h_1 + 1:
    print('YES')
elif v_2 == v_1 + 1 and h_2 == h_1 - 1:
    print('YES')
elif v_2 == v_1 - 1 and h_2 == h_1 - 1:
    print('YES')
else:
    print('NO')

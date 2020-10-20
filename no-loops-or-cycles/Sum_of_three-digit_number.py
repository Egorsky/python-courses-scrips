#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User enters three-digit number and program prints sum of digits"""


num = int(input())
print((num % 10) + (num // 10 % 10) + (num // 100))

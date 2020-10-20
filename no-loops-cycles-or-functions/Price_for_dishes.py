#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A dish has a price of a - dollars and b - cents. User enter the price
   and the number of servings. Program prints the amount of money user
   should pay."""


a = int(input())
b = int(input())
n = int(input())
price = a * 100 + b
payRub = (price * n) // 100
payCop = (price * n) % 100
print(payRub, payCop)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Two points in time are given within the same day. The hour, minute and second are indicated for each moment. 
   It is known that the second moment of time did not come earlier than the first. The user enters the amount of
   hours, minutes and seconds for each period of time. The program prints how many seconds are between those
   periods."""


h1 = int(input())  # an amount of hours for the first period of time
m1 = int(input())  # an amount of minutes for the first period of time 
s1 = int(input())  # an amount of seconds for the first period of time
h2 = int(input())
m2 = int(input())
s2 = int(input())
time1 = s1 + m1 * 60 + h1 * 3600  # recalculating 1st time period into seconds
time2 = s2 + m2 * 60 + h2 * 3600  # recalculating 2nd time period into seconds
print(time2 - time1)

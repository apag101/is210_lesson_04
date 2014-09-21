#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LESSON4:
TASK4
Practice looping math calculations."""

import data
TEAM1 = []
TEAM2 = []
TEAM3 = []
name = [] 
name2 = []
connect = []

for n in data.MULTIPLAYERS.split("\n"):
    name.append(n)
count = 0
while count < 20:
    for i in name:
        name2.append(name[count][0:12].strip())
        count += 1
count = 0
while count < 20:
    for c in name:
        connect.append(name[count][12:].strip())
        count += 1
count = 1
count2 = 1
while count < 20:
    if int(connect[count]) == 1:
        while count2 < 5:
            TEAM1.append(name2[count])
            count += 1
            TEAM2.append(name2[count])
            count += 1
            TEAM3.append(name2[count])
            count += 1
            count2 += 1
        else:break
    else:break
print "TEAM 1 includes {0}". format(TEAM1)
print "TEAM 2 includes {0}". format(TEAM2)
print "TEAM 3 includes {0}". format(TEAM3)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LESSON4:
TASK4
Practice looping math calculations."""

import data
TEAM1 = []
TEAM2 = []
TEAM3 = []
NAME = []
NAME2 = []
CONNECT = []

for n in data.MULTIPLAYERS.split("\n"):
    NAME.append(n)
COUNT = 0
while COUNT < 20:
    for i in NAME:
        NAME2.append(NAME[COUNT][0:12].strip())
        COUNT += 1
COUNT = 0
while COUNT < 20:
    for c in NAME:
        CONNECT.append(NAME[COUNT][12:].strip())
        COUNT += 1
COUNT = 1
COUNT2 = 1
while COUNT < 20:
    if int(CONNECT[COUNT]) == 1:
        while COUNT2 < 5:
            TEAM1.append(NAME2[COUNT])
            COUNT += 1
            TEAM2.append(NAME2[COUNT])
            COUNT += 1
            TEAM3.append(NAME2[COUNT])
            COUNT += 1
            COUNT2 += 1
        else: break
    else:
        break
print "TEAM 1 includes {0}". format(TEAM1)
print "TEAM 2 includes {0}". format(TEAM2)
print "TEAM 3 includes {0}". format(TEAM3)

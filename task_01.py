#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LESSON4:
TASK1
Practice analyzing strings."""

import data
print data.SHAKESPEARE
LI = []
for l in data.SHAKESPEARE.split("\n"):
    LI.append(len(l))
MAXIMUM_WORDS = sorted(LI, reverse=True)[0]
MINIMUM_WORDS = sorted(LI)[0]
AVERAGE_WORDS = sum(LI) / float(len(LI))

LA = []
COUNT = 0
for a in data.SHAKESPEARE.split("\n"):
    LA.append(a)
for i in LA:
    if "Crispian" in i:
        COUNT += 1
NUM_CRISPIAN = COUNT

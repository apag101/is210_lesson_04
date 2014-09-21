#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LESSON4:
TASK3
Practice looping math calculations."""

import data
s = []
for d in data.TRANSACTIONS:
    s += [sum(d)]
TOTAL = sum(s)
MINIMUM = sorted(s)[0]
MAXIMUM = sorted(s, reverse = True)[0]

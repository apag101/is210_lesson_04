#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LESSON4:
TASK3
Practice looping math calculations."""

import data
S = []
for d in data.TRANSACTIONS:
    S += [sum(d)]
TOTAL = sum(S)
MINIMUM = sorted(S)[0]
MAXIMUM = sorted(S, reverse=True)[0]

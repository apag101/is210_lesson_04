#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LESSON4:
TASK5
Practice create versus Matchups."""

import data
MATCHUPS = ('')
allm = []
for ROW_INDEX, ROW_NAME in enumerate(data.VERSUS):
    for COLUMN_INDEX, COLUMN_NAME in enumerate(data.VERSUS):
        if ROW_INDEX > COLUMN_INDEX or ROW_INDEX < COLUMN_INDEX:
            allm.append('{0}, {1}, {2}'.format(COLUMN_INDEX, ROW_NAME, COLUMN_NAME).strip())
            MATCHUPS = (allm)
        else: break

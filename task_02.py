#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LESSON4:
TASK2
Practice prompting inside a loop."""

import data
ACCESS = False
count = 0
REPLIES = ["Not correct", "Umm Yes ?", "I do not remember"]
TRACK = [3, 2, 1]

while ACCESS == False:
    password = raw_input("What is your password ({0} attempts left)?".format(TRACK[count]))
    if password not in data.PASSWORD:
        print REPLIES[count]
        count += 1
        if count > 2:
            print "Access is denied, please try again later."
            break
    else:
        ACCESS == True
        break

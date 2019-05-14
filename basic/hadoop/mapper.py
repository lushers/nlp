#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2019 mobvoi.com, Inc. All Rights Reserved
#
########################################################################
"""
File: mapper.py
Date: 2019/05/14 11:07:24
"""
import sys
from numpy import mat, mean, power

def read_input(file):
    for line in file:
        yield line.strip()

input = read_input(sys.stdin)
input = [float(line) for line in input]
numInput = len(input)
input = mat(input)
sqInput = power(input, 2)

print "%d\t%f\t%f" % (numInput, mean(input), mean(sqInput))
print >> sys.stderr, "report, still alive"

#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2019 mobvoi.com, Inc. All Rights Reserved
#
########################################################################
"""
File: reducer.py
Date: 2019/05/14 11:15:31
"""
import sys
from numpy import mat, mean, power

def read_input(file):
    for line in file:
        yield line.strip()

input = read_input(sys.stdin)
mapperOut = [line.split('\t') for line in input]
cumVal = 0.0
cumSumSq = 0.0
cumN = 0.0

for instance in mapperOut:
    nj = float(instance[0])
    cumN += nj
    cumVal += nj * float(instance[1])
    cumSumSq += nj * float(instance[2])

means = cumVal / cumN
varSum = (cumSumSq - 2 * means * cumVal + cumN * means * means) / cumN

print "%d\t%f\t%f" % (cumN, means, varSum)
print >> sys.stderr, "report: reducer still alive"

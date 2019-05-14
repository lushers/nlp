#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2019 mobvoi.com, Inc. All Rights Reserved
#
########################################################################
"""
File: baby_softmax.py
Date: 2019/05/13 17:18:30
"""
import numpy as np

def softmax(X):
    exps = np.exp(X)
    return exps / np.sum(exps)

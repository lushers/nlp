#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2019 mobvoi.com, Inc. All Rights Reserved
#
########################################################################
"""
File: o.py
Date: 2019/05/11 17:55:25
"""
import numpy as np

a = np.random.standard_normal((1, 500))
x = np.arange(0,50,0.1)
y =  x**2 + x*2 + 5
y = y - a*100
y = y[0]
x1 = x * x

#归一化
def scaling(x,x1):
    n_x = (x - np.mean(x))/50
    n_x1 = (x1 - np.mean(x))/2500
    return n_x,n_x1


def Optimization(x,x1,y,theta,learning_rate):
    for i in range(iter):
        theta = Updata(x,x1,y,theta,learning_rate)
    return theta
 
def Updata(x,x1,y,theta,learning_rate):
    m = len(x1)
    sum = 0.0
    sum1 = 0.0
    sum2 = 0.0
    n_x,n_x1 = scaling(x,x1)
    alpha = learning_rate
    h = 0
    for i in range(m):
        h = theta[0] + theta[1] * x[i] +theta[2] * x1[i]
        sum += (h - y[i])
        sum1 += (h - y[i]) * n_x[i]
        sum2 += (h - y[i]) * n_x1[i]
    theta[0] -= alpha * sum / m 
    theta[1] -= alpha * sum1 / m 
    theta[2] -= alpha * sum2 / m 
    return theta
#数据初始化
 
learning_rate = 0.0001
theta = [0,0,0]

for i in range(3000):
    print Updata(x,x1,y,theta,learning_rate)



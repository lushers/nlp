#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2019 mobvoi.com, Inc. All Rights Reserved
#
########################################################################
"""
File: x.py
Date: 2019/05/11 16:58:35
"""
import random

data = []

def data_gen(n):
    """
    生成一些x2 的数据
    """
    for i in range(n):
        x = random.random()
        y = 2.5* x * x
        data.append((x, y))


def param_train(n):
    """
    已知为2阶, 求解参数
    y = w0 + w1 * x + w2 * x * x
    J(w) = 1 / 2 * sum_n((y(w, x_n) - t_n))
    """
    # 随机化参数
    w0 = 0 #random.random()
    w1 = 0 #random.random()
    w2 = 0 #random.random()
    learning_rate = 0.000001
    batch = 10

    for i in range(n):
        for bn in range(len(data) / batch):
            delta_J0 = 0
            delta_J1 = 0
            delta_J2 = 0
            for ite in range(batch):
                k = bn * batch + ite
                h = (w0 + w1 * data[k][0]+ w2 * data[k][0] * data[k][0] - data[k][1])
                delta_J0 += h * 1
                delta_J1 += h * data[k][0]
                delta_J2 += h * 2 * data[k][0]
                print delta_J0, delta_J1, delta_J2
            w0 -= learning_rate * delta_J0 / batch
            w1 -= learning_rate * delta_J1 / batch
            w2 -= learning_rate * delta_J2 / batch
            print w0, w1, w2
    print w0, w1, w2


if __name__ == "__main__":
    data_gen(100)
    param_train(1000)

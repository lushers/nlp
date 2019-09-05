#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2019 sina.com.cn, Inc. All Rights Reserved
#
########################################################################
"""
File: change.py
Author: qinchuan1(qinchuan1@staff.sina.com.cn)
Date: 2019/09/04 23:50:28
"""
class data(object):
    """
    数据类:
        part: 受试者
        task: 任务
        text_type: 任务类型
        key: 豆豆
        dur_sec: 豆豆1
        fixA: 豆豆2
        trtA: 豆豆3
    """
    def __init__(self, part, task, text_type, key, dur_sec, fixA, trtA):
        self.part = part
        self.task = task
        self.text_type = text_type
        self.key = key
        self.dur_sec = dur_sec
        self.fixA = fixA
        self.trtA = trtA

def dels(obj1, obj2):
    key = str(obj2.key - obj1.key)
    dur_sec = str(obj2.dur_sec - obj1.dur_sec)
    fixA = str(obj2.fixA - obj1.fixA)
    trtA = str(obj2.trtA - obj1.trtA)
    return '\t'.join([key, dur_sec, fixA, trtA])

with open('./Gap.txt') as fd:
    obj_lists = []
    for line in fd:
        if line.startswith('Part'):
            continue
        lists = line.strip().split('\t')
        obj = data(
            part=lists[0],
            task=lists[1],
            text_type=lists[2],
            key=float(lists[3]),
            dur_sec=float(lists[4]),
            fixA=float(lists[5]),
            trtA=float(lists[6])
        )
        obj_lists.append(obj)
    # 处理
    results = []
    part_res = []
    flag = ''
    for i, unit in enumerate(obj_lists):
        if unit.part != flag:
            # 一位受试者结束, 开始计算
            if len(part_res) == 4:
                t_p1 = dels(part_res[0], part_res[2])
                t_p2 = dels(part_res[1], part_res[3])
                results.append('')
                results.append('')
                results.append(t_p1)
                results.append(t_p2)
            part_res = []
            part_res.append(unit)
            flag = unit.part
        else:
            part_res.append(unit)
    if len(part_res) == 4:
        t_p1 = dels(part_res[0], part_res[2])
        t_p2 = dels(part_res[1], part_res[3])
        results.append('')
        results.append('')
        results.append(t_p1)
        results.append(t_p2)
    for unit in results:
        print unit












#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Copyright (c) 2019 mobvoi.com, Inc. All Rights Reserved
#
########################################################################
"""
File: max_forward.py
Date: 2019/05/09 11:30:20
brief: 最大正向匹配分词
"""
windows = 5

def reading(file_name):
    """
    读文件
    """
    lists = []
    with open(file_name) as fd:
        for line in fd:
            uline = line.strip().decode('utf-8')
            lists.append(uline)
    return lists


def gen_dict(file_name):
    """
    生成词典
    """
    lists = reading(file_name)
    word_dict = set(lists)
    return word_dict

def max_forward(string, word_dict):
    """
    最大正向
    """
    string = string.decode('utf-8')
    end = 0
    idx = 0
    matched = False
    words = []
    while end < len(string):
        matched = False
        for i in xrange(windows, 0, -1):
            s = string[idx:idx+i]
            if s in word_dict:
                matched = True
                words.append(s)
                end = idx + i -1
                idx = end + 1
                # print 'in', idx, end
                break
        if not matched:
            if idx < len(string):
                words.append(string[idx])
            idx += 1
            end += 1
            # print 'notin', idx, end
    return words


if __name__ == '__main__':
    word_dict = gen_dict('./dict.txt')
    asd = max_forward('你这个傻逼，我操!', word_dict)
    for s in asd:
        print s.encode('utf-8')

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/10/31
# By Charlotte.HonG
# unix_mid_test_07


def drawing_triangle(str, l, t):
    graph = ''
    # 取得正負號
    sign = int(l / (l * l) ** 0.5)
    # 修正參數(負號需-1)
    revise = (sign - (l / l)) / 2
    # 起始與結束值
    end = ((l * sign) + l) / 2
    start = end - l
    # 圖形
    for j in xrange(start + revise, end + revise, sign):
        for i in xrange(0, j + 1):
            graph += str
        graph += '\n'
    return graph


def main():
    print drawing_triangle('*', -5, 1)


def drawing_diamond(str, x, y):
    graph = ''
    for j in xrange(0, y):
        for i in xrange(j + 1, y):
            graph += ' '
        for i in xrange(0, 2 * j + 1):
            graph += str
        graph += '\n'
    for j in xrange(y - 2, -1, -1):
        for i in xrange(j + 1, y):
            graph += ' '
        for i in xrange(0, 2 * j + 1):
            graph += str
        graph += '\n'
    return graph

if __name__ == '__main__':
    main()

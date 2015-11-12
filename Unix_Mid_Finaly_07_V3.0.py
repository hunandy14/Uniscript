#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/10/31
# By Charlotte.HonG
# unix_mid_test_07


# 圖形核心
# str=構成圖形的字元,l=行數
# t=遞減或遞增(*只能為 1 or -1 )
# s=每行前面的空格數
def drawing_triangle(str, l, t, s):
    graph = ''
    # 取得正負號
    sign = int(l / (l * l) ** 0.5)
    # 取絕對值
    l = int((l ** 2) ** 0.5)
    # 修正參數(負號需-1)
    revise = (t - (t / t)) / 2
    # 起始與結束值
    end = ((l * t) + l) / 2
    start = (end - l) * t
    # 圖形
    for j in xrange(start + revise, end + revise, t):
        # 每行的空格
        for i in xrange(0, s):
            graph += ' '
        # 向右對齊
        if sign < 0:
            for i in xrange(j + 1, l):
                graph += ' '
        # 主要文字
        for i in xrange(0, j + 1):
            graph += str
        graph += '\n'
    return graph


# 驅動圖形
def draw(sym, l, t):
    str = ''
    space = 0
    if t == 1:
        str += drawing_triangle(sym, l, 1, space)
    if t == 2:
        str += drawing_triangle(sym, l, -1, space)
    if t == 3:
        str += drawing_triangle(sym, (l - 1) / 2, 1, space)
        # 修正參數
        if l < 0:
            space += 1
        str += drawing_triangle(sym, (l - 1) / 2 + 1, -1, space)
    return str


def main():
    print draw('=', 3, 1)
    print draw('*', 5, 2)
    print draw('#', -9, 3)
    # 或是只有 draw(sym,l,t)


if __name__ == '__main__':
    main()

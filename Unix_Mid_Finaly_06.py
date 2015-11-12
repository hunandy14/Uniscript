#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/11/06
# By Charlotte.HonG
# unix_mid_test_06


# 乘法核心
def mt_kernel(x1, x2, y):
    mt = ''
    # 高度
    for j in xrange(1, y + 1):
        # 寬度
        for i in xrange(x1, x2 + 1):
            mt += str(i) + 'x' + str(j)
            # 處理雙位數對齊
            if i * j < 10:
                mt += '= '
            else:
                mt += '='
            mt += str(i * j) + '     '
        mt += '\n'
    return mt


# 驅動乘法
def mt(x, y, n):
    str = ''
    row = x / n + 1  # 高度
    rem = int(x % n)  # 餘數(最後一排有幾個)
    # 幾排都是整齊的
    for i in xrange(0, row - 1):
        str += mt_kernel(i * n + 1, (i + 1) * n, y) + '\n'
    # 最後一排額外處理
    str += mt_kernel(x - rem + 1, x, y)
    return str


def main():
    print mt(7, 5, 9)
    print mt(7, 5, 6)
    print mt(7, 5, 2)
    print mt(7, 5, 1)
    # 或是只有 mt(j, i, n)


if __name__ == '__main__':
    main()

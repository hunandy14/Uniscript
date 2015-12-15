#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/10/31
# By Charlotte.HonG
# unix_mid_test_05


import random


# 演算法
# def insertion_sort(lst, start, end):
#     if len(lst) == 1:
#         return
#     for i in xrange(start + 1, end + 1):
#         temp = lst[i]
#         j = i - 1
#         while j >= start and temp < lst[j]:
#             lst[j + 1] = lst[j]
#             j -= 1
#         lst[j + 1] = temp


# 使用內建函數
def sortsl(lst, start, end):
    temp_list = lst[start:end + 1]
    temp_list.sort()
    temp_list = lst[:start] + temp_list + lst[end + 1:]
    return temp_list


def main():
    random_list = range(0, 10)
    random.shuffle(random_list)
    print 'Original=   ', random_list
    print 'Limit_Order=', sortsl(random_list, 1, 8)
    print 'Original=   ', random_list


if __name__ == '__main__':
    main()

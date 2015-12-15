#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/10/31
# By Charlotte.HonG
# unix_mid_test_01


def rm_all(l1, l2):
    l_last = l1[:]
    for i in xrange(0, len(l2)):
        l_last.remove(l2[i])
    return l_last


def main():
    list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [2, 4, 6, 8]
    print list1
    print list2
    print rm_all(list1, list2)


if __name__ == '__main__':
    main()

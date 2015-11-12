#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/10/31
# By Charlotte.HonG
# unix_mid_test_03_V2.0


def rm_dup(l):
    for i in xrange(len(l) - 1, 0, -1):
        if l[i] == l[i - 1]:
            del l[i:i + 1]


def main():
    list1 = [0, 1, 2, 3, 1, 1, 1, 1, 1]
    list2 = [1, 1, 2, 2, 3, 3, 5, 4, 1, 1]
    rm_dup(list1)
    print 'list1=', list1
    rm_dup(list2)
    print 'list2=', list2


if __name__ == '__main__':
    main()

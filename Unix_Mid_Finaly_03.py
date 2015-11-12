#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/10/31
# By Charlotte.HonG
# unix_mid_test_03


def rm_dup(l):
    temp_l = []
    for i in xrange(0, len(l) - 1):
        if l[i] == l[i + 1]:
            temp_l.append(i)
    for i in xrange(0, len(temp_l)):
        del l[temp_l[-i]:temp_l[-i] + 1]


def main():
    list1 = [0, 1, 2, 3, 1, 1, 1, 1, 1]
    list2 = [1, 1, 2, 2, 3, 4, 5, 1, 1]
    rm_dup(list1)
    print 'list1=', list1
    rm_dup(list2)
    print 'list2=', list2


if __name__ == '__main__':
    main()

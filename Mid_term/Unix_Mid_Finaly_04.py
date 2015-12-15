#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/10/31
# By Charlotte.HonG
# unix_mid_test_04


import random


def permu(l):
    random.shuffle(l)


def main():
    num = range(0, 10)
    print 'original=', num
    for i in xrange(0, 3):
        permu(num)
        print num


if __name__ == '__main__':
    main()

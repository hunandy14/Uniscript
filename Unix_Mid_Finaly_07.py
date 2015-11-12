#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/10/31
# By Charlotte.HonG
# unix_mid_test_07


def drawing(str, x, y):
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


def main():
    print drawing('*', 4, 5)


if __name__ == '__main__':
    main()

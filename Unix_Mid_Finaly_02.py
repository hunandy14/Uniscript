#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/10/31
# By Charlotte.HonG
# unix_mid_test_02


def is_palindrome(s):
    return s == s[::-1]


def main():
    list1 = [1, 2, 3, 2, 1]
    list2 = [1, 2, 3, 3, 2, 1]
    list3 = ['a', 'b', 'b', 'a']
    list4 = ['a', 'b', 'a', 'b']
    list5 = [1, 2, 3, 4, 5]
    print is_palindrome(list1)
    print is_palindrome(list2)
    print is_palindrome(list3)
    print is_palindrome(list4)
    print is_palindrome(list5)


if __name__ == '__main__':
    main()

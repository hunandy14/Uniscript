#!/usr/bin/python
# -*- coding: utf-8 -*-
# Date 2015/10/31
# By Charlotte.HonG
# unix_mid_test_07
# UpdateData 2015/11/08


# 依序導入排序法
def multi_merge(l):
    multi_list = l[0][:]
    multi_list = merge(multi_list, l[1])
    multi_list = merge(multi_list, l[2])
    return multi_list


# 排序法核心
def merge(list1, list2):
    list = list1[:]
    count = 0   # 編號(比過的不用重比) + 計算複雜度
    flag = 0    # 例外處理
    # 將陣列依序導入
    for j in xrange(0, len(list2)):
        # 陣列2依序與陣列1比較
        for i in xrange(count, len(list)):
            count += 1
            flag = 1
            # 如果小於就插入
            if list2[j] <= list[i]:
                list.insert(i, list2[j])
                flag = 0
                break
        # 如果標記沒有清除，表示有值沒有被放入
        if flag == 1:
            count += 1
            # 剩下的不用比對直接放入
            list += list2[j:]
            break
    # 確認複雜度
    print 'setup count=', count
    return list


def main():
    l = [[1, 3, 5, 7, 9, 10],
         [2, 2, 4, 6, 8, 11, 12],
         [90, 91, 92, 93, 94, 95]]
    print l
    print 'result =', multi_merge(l)


if __name__ == '__main__':
    main()

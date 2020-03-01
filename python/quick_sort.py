#!/usr/bin/env python
# encoding: utf-8


def quick_sort(l, left, right):
    if left < right:
        i = partition(l, left, right)
        quick_sort(l, left, i - 1)
        quick_sort(l, i + 1, right)


def partition(l, left, right):
    base = l[left]
    while left < right:
        while left < right and l[right] >= base:
            right = right - 1
        l[left] = l[right]
        while left < right and l[left] <= base:
            left = left + 1
        l[right] = l[left]

    l[left] = base
    return left


def partition1(l, left, right):
    # 拿最后当基准
    base = l[right]
    i = left - 1
    for j in range(left, right):
        if l[j] <= base:
            i += 1
            # 交换i,j
            l[i], l[j] = l[j], l[i]
            print l
    # 交换最后一个
    l[i + 1], l[right] = l[right], l[i + 1]
    return i + 1


a = [1, 8, 5, 7, 4, 9, 2]
quick_sort(a, 0, len(a) - 1)
print(a)

#!/usr/bin/env python
# encoding: utf-8

def merge_sort(unsorted):
    size = len(unsorted)
    if size == 1:
        return unsorted
    mid = size / 2 + size % 2
    a = unsorted[:mid]
    b = unsorted[mid:]

    a = merge_sort(a)
    b = merge_sort(b)

    result = []
    while a != [] and b != []:
        if a[0] < b[0]:
            result.append(a[0])
            a.pop(0)
        else:
            result.append(b[0])
            b.pop(0)
    result.extend(a)
    result.extend(b)
    return result

k = [1,3,5,6,7,1,990,6]
print merge_sort(k)

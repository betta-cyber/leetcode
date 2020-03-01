#!/usr/bin/env python
# encoding: utf-8

def binary_search(blist, item):
    low = 0
    high = len(blist)-1
    while low <= high:
        mid = low + (high-low)/2
        if blist[mid] >= item:
            high = mid - 1
        if blist[mid] < item:
            low = mid + 1
    return low

def binary_search_no_double(blist, item):
    low = 0
    high = len(blist)-1
    while low <= high:
        mid = low + (high-low)/2
        if blist[mid] > item:
            high = mid - 1
        if blist[mid] < item:
            low = mid + 1
        if blist[mid] == item:
            return mid
    return low


l = [2,5,6,7,11,13,13,16,18,64,77,79]
print binary_search(l, 13)

#!/usr/bin/env python
# encoding: utf-8

import heapq

def get_max_heap(heap, size, root):
    left = 2 * root + 1
    right = left + 1
    larger = root

    if left < size and heap[larger] < heap[left]:
        larger = left
    if right < size and heap[larger] < heap[right]:
        larger = right
    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]
        get_max_heap(heap, size, larger)


# 构建最大堆
def build_heap(heap):
    for index in xrange(len(heap)/2-1, -1, -1):
        get_max_heap(heap, len(heap), index)


def sort(heap):
    build_heap(heap)
    for index in xrange(len(heap)-1, -1, -1):
        print heap
        heap[0], heap[index] = heap[index], heap[0]
        get_max_heap(heap, index, 0)
    return heap

a = [4,6,7,41,999,234,734]
print sort(a)

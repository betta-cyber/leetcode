#!/usr/bin/env python
# encoding: utf-8
# Use function kthSmall to find the kth smallest number in A and B. Make sure list A is shorter (if lenA - i1 > lenB - i2: return kthSmall(B, A, i2, i1, k)).
# i1 and i2 are the starting points for A and B. If i1 is 0, pa is 2, i2 is 0, pb is 3 (k = 5) and A[1] < B[2], then we can safely ignore A[0] and A[1] since A[0] <= A[1],
# B[0] <= B[1] <= B[2].

def findMedianSortedArrays(self, A, B):
    def kthSmall(A, B, i1, i2, k):
        lenA, lenB = len(A), len(B)
        if i1 >= lenA: return B[k - 1]
        if i2 >= lenB: return A[k - 1]
        if k == 1: return min(A[i1], B[i2])
        if lenA - i1 > lenB - i2: return kthSmall(B, A, i2, i1, k)
        pa = min(lenA - i1, k / 2)
        pb = k - pa
        return kthSmall(A, B, i1 + pa, i2, pb) if A[i1 + pa - 1] < B[i2 + pb - 1] else kthSmall(A, B, i1, i2 + pb, pa)

    lenAB = len(A) + len(B)
    return kthSmall(A, B, 0, 0, lenAB / 2 + 1) if lenAB % 2 else 0.5 * (kthSmall(A, B, 0, 0, lenAB / 2) + kthSmall(A, B, 0, 0, lenAB / 2 + 1))


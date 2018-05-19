#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def removeDuplicates(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        # write your code here
        k=0
        for i in range(1,len(A)):
            if A[i] != A[k]:
                k+=1
                A[k] = A[i]

        del A[k+1:len(A)]
        return len(A)

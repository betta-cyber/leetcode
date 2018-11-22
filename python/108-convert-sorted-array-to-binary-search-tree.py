#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums)-1)


    def helper(self, nums, l, r):
        if (l > r):
            return None
        else:
            mid = (r-l)/2 + l
            midNode = TreeNode(nums[mid])
            midNode.left = self.helper(nums, l, mid-1)
            midNode.right = self.helper(nums, mid+1, r)

            return midNode

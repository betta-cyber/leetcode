class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        curv = maxv = minv = nums[0]
        res = [curv]
        for i in nums[1:]:
            curv = i
            # 当前的最大值等于已知的最大值、最小值和当前值的乘积，当前值，这三个数的最大值
            a = maxv*curv
            # 当前的最小值等于已知的最大值、最小值和当前值的乘积，当前值，这三个数的最小值。
            b = minv*curv
            maxv = max(curv, a, b)
            minv = min(curv, a, b)
            res.append(maxv)
        
        # 结果是最大值数组中的最大值。
        return max(res)
        

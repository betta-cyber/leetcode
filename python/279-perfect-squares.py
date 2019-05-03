class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]
        for i in range(1, n+1):
            j = 1
            res = []
            while j*j <= i:
                res.append(dp[i - j*j] + 1)
                j += 1
            dp.append(min(res))
        return dp[-1]

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


"""
Solution 1: DP
dp[i] := ans
dp[0] = 0
dp[i] = min{dp[i – j * j] + 1} 1 <= j * j <= i

dp[5] = min{
dp[5 – 2 * 2] + 1 = dp[1] + 1 = (dp[1 – 1 * 1] + 1) + 1 = dp[0] + 1 + 1 = 2,
dp[5 – 1 * 1] + 1 = dp[3] + 1 = (dp[3 – 1 * 1] + 1) + 1 = dp[1] + 2 = dp[1 – 1*1] + 1 + 2 = dp[0] + 3 = 3
};

dp[5] = 2

Time complexity: O(n * sqrt(n))
Space complexity: O(n)
"""

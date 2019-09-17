class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        a = [1]
        b = []
        
        last = 1
        for i in range(1, length):
            last = nums[i - 1] * last
            a.append(last)
        
        last = 1
        for k in range(length-1)[::-1]:
            last = last * nums[k + 1]
            b.append(last)
    
        b = b[::-1]
        b.append(1)
        res = []
        for i in range(length):
            res.append(a[i] * b[i])
            
        return res

#我们以一个4个元素的数组为例，nums=[a1,a2,a3,a4]，要想在O(n)的时间内输出结果，比较好的解决方法是提前构造好两个数组：
#[1, a1, a1*a2, a1*a2*a3]
#[a2*a3*a4, a3*a4, a4, 1]
#然后两个数组一一对应相乘，即可得到最终结果 [a2*a3*a4, a1*a3*a4, a1*a2*a4, a1*a2*a3]。

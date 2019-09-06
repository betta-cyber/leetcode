class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = []
        r = 0
        flag = False
        if abs(x) > 2**31:
            return 0
        if x >= 0:
            x = x
        else:
            x = -x
            flag = True

        while x != 0:
            q = x % 10
            x = x/10
            res.append(q)

        for index, item in enumerate(res):
            r += item * pow(10, (len(res)-index-1))

        if abs(r) > 2**31:
            return 0
        if flag:
            return -r
        else:
            return r

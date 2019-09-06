# -*- coding: utf-8 -*-


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return self.do(digits)

    def do(self, digits):
        if digits:
            d = digits.pop()
        else:
            d = 0
        if d < 9:
            d += 1
            digits.append(d)
            return digits
        else:
            res = self.do(digits)
            res.append(0)
            return res

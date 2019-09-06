# -*- coding: utf-8 -*-


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a)
        b = list(b)

        carry = 0
        res = []

        while a or b:
            if a:
                ai = a.pop()
            else:
                ai = 0
            if b:
                bi = b.pop()
            else:
                bi = 0
            cur = int(ai) + int(bi) + carry
            if cur > 1:
                carry = 1
                cur = cur - 2
            else:
                carry = 0
            res.append(cur)

        if carry > 0:
            res.append(1)

        k = ""
        for i in res[::-1]:
            k += str(i)

        return k

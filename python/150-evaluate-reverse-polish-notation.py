#!/usr/bin/env python
# encoding: utf-8

# 波兰表达式的实现，用栈，就是不知道为什么速度不咋地，需要注意的就是/的时候负数有点小坑

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in ['+', '-', '*', "/"]:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                res = self.cul(a, b, i)
                stack.append(res)
        return stack[-1]

    def cul(self, a, b, op):
        if op == '+':
            return b+a
        if op == '-':
            return b-a
        if op == '*':
            return b*a
        if op == '/':
            if a*b < 0 and b % a != 0:
                return b/a+1
            else:
                return b/a

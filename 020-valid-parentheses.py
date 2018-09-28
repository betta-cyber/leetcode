#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        print stack
        print(s)
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if stack != []:
                    if stack.pop() <> "(":
                        return False
                else:
                    return False
            if s[i] == ']':
                if stack != []:
                    if stack.pop() <> "[":
                        return False
                else:
                    return False
            if s[i] == '}':
                if stack != []:
                    if stack.pop() <> "{":
                        return False
                else:
                    return False
        if stack:
            return False
        if not stack:
            return True

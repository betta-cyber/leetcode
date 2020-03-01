class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = s.split(" ")
        index = -1
        while 1:
            try:
                if st[index]:
                    return len(st[index])
                else:
                    index -= 1
            except Exception:
                return 0
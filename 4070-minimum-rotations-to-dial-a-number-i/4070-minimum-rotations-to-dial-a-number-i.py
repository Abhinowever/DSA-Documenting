class Solution(object):
    def minRotations(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        last = 0
        for i in s :
            result += min(abs(last-int(i)), 10 - abs(last-int(i)))
            # result += min(current,10-current)
            last = int(i)
        return result 
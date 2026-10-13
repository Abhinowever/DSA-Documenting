from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        total_s = Counter(s)
        total_t = Counter(t)
        return total_s == total_t
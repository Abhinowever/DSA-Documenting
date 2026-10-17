class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        front, reverse = {},{}
        for i in range(len(s)) :
            if s[i] in front :
                if front[s[i]] != t[i] :
                    return False
            else :
                if t[i] in reverse :
                    return False
                reverse[t[i]] = s[i]
                front[s[i]] = t[i]
        return True
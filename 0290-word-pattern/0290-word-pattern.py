class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")
        front,reverse = {},{}
        
        if len(s) != len(pattern) :
            return False
        
        for i in range(len(s)) :
            if s[i] in front :
                if front[s[i]] != pattern[i] :
                    return False
            else : 
                if pattern[i] in reverse :
                    return False
                front[s[i]] = pattern[i]
                reverse[pattern[i]] = s[i]
        return True
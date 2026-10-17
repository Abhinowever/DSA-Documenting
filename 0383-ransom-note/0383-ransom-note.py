from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        list1,list2 = defaultdict(int),defaultdict(int)
        for i in ransomNote :
            list1[i] += 1
        for i in magazine :
            list2[i] += 1
        result = True
        for i in list1 :
            if list2[i] < list1[i] :
                result = False
                break
        return result
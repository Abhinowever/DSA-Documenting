class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        temp = {}
        for i in arr :
            if i in temp :
                temp[i] += 1
            else :
                temp[i] = 1
                
        new = set(temp.values())

        return len(new) == len(temp)
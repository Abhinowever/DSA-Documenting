class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nonZERO = False
        total = 0
        left,right = 0,0
        for x in nums :
            total ^= x
            if x != 0:
                nonZERO = True
        if total != 0 :
            return len(nums)
        if nonZERO :
            return len(nums) -1
        return 0
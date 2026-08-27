class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        maxx = 0

        for i in range(len(nums)):
            if i > maxx :
                return False
            if (i + nums[i]) > maxx :
                maxx = i + nums[i]
        return True
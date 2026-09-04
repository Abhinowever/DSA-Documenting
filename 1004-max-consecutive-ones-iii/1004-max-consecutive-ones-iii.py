class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        for right, i in enumerate(nums):
            if i == 0:
                k -= 1
            if k < 0 :
                k += 1 - nums[left]
                left += 1
        return len(nums) - left
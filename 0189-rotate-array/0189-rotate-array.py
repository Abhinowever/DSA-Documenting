class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)

        if k == 0 :
            return nums

        nums[:] = nums[-k:] + nums[:-k]
        
        # print(n)
        # if len(nums) > 50000 :
        #     break 
        # for _ in range(n):
        #     nums.insert(0,nums.pop())
 
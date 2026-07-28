class Solution(object):
    def minArraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Set = set(nums)
        pelnorazi = nums[:]

        minn = min(nums)
        total = 0
        for x in nums:
            if x % minn == 0:
                total += minn
                continue
            best = x
            for i in range(1, int(x**0.5) + 1):
                if x % i == 0:
                    if i in Set:
                        best = i
                        break
                    target = x // i
                    if target in Set:
                        best = min(best, target)
                        
            total += best

        return total
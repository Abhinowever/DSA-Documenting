# from math import prod
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        zero = 0
        prod = 1

        for i in nums :
            if i != 0 :
                prod *= i
            else :
                zero += 1
        
        if zero == 0 :
            return [prod//i for i in nums]
        elif zero == 1 :
            return [0 if i!=0 else prod for i in nums]
        else :
            return [0]* len(nums)
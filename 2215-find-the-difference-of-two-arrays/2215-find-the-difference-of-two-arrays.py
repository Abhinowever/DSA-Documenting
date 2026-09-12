class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        first,second = set(nums1),set(nums2)
        new1,new2 = [],[]
        for i in first :
            if i not in second :
                new1.append(i)
        for i in second :
            if i not in first :
                new2.append(i)

        return [new1,new2]
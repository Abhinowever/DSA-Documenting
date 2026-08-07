class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # lmax
        # rmax

        # water = 0
        # s = len(height)
        # i = 1
        # while i < s-1:

        #     lmax = max(height[0:i])
        #     rmax = max(height[i+1:s])
        #     units = min(lmax,rmax)

        #     curr = (units - height[i]) if units > height[i] else 0 

        #     water += curr

        #     i += 1
        #     # print(water)

        # return water

        n = len(height)
        if n == 0:
            return 0

        left = [0] * n
        right = [0] * n

        max_left = 0
        for i in range(n):
            max_left = max(max_left, height[i])
            left[i] = max_left

        max_right = 0
        for i in reversed(range(n)):
            max_right = max(max_right, height[i])
            right[i] = max_right

        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]

        return water
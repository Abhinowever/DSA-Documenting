class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        left,right = 0,l-1
        max_area = current_area = 0
        while left < right :
            minimum = min(height[left],height[right])
            current_area = minimum * (right - left)
            if current_area > max_area :
                max_area = current_area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area
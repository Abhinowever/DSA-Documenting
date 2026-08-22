class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxx = 0
        
        heights.append(0) # adding this will results in traversion of all the elements.

        for i ,h in enumerate(heights) :

            while stack and heights[stack[-1]] > h : # weather the current bar is shorter than the last bigger bar

                height = heights[stack.pop()] # calculating the maximum area could be get by the recent largest bar


                if stack :
                    width = i - stack[-1] - 1 # i -> next smaller, stack[-1] -> previous smaller 
                else :
                    width = i
                
                maxx = max(maxx,height * width)

            stack.append(i)
        
        return maxx
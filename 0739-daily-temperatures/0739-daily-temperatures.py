class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        l = len(temperatures)
        arr = [0]*l
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                idx = stack.pop()
                arr[idx] = i - idx
            stack.append(i)

        return arr

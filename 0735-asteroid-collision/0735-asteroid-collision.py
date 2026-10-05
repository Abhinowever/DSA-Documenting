class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in asteroids :
            while stack and stack[-1] > 0  and 0 > i :
                if stack[-1] < -i :
                    stack.pop()
                elif stack[-1] == -i:
                    stack.pop()
                    break
                else :
                    break
            else :
                stack.append(i)    
        return stack
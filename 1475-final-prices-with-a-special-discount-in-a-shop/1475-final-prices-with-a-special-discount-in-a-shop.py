class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        l = len(prices)
        ans = prices[:]
        stack = []          
        for i in range(l):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                ans[idx] = prices[idx] - prices[i]  
            stack.append(i)
        return ans

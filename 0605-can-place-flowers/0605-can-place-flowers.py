class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        for i in range(l):
            if n > 0 and flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
        return n <= 0




















        # series = flowerbed[:]
        # if series[0] == 0 and series[1] == 0:
        #         series[0] = 1
        #         n -= 1
        # for i in range(1,l-1):
        #     if series[i] == 0 :
        #         if series[i-1] == 0 and series[i+1] == 0:
        #             series[i] = 1
        #             n -= 1
        # if n > 0 and series[-1] == 0 and series[-2] == 0:
        #     series[-1] = 1
        #     n-= 1
        # print(series)

        # return n == 0
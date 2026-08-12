class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """

        x = int(str(n)[::-1])
        summ = 0
        a = min(x,n)
        b = max(x,n)
        def isPrime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            
            return True
        for i in range(a,b+1):
            if isPrime(i):
                summ += i

        return summ
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        N = numRows
        if numRows == 1 or numRows >= len(s):
            return s
        res = ""

        for n in range(N):
            i = n
            f = True

            while i < len(s) :
                res += s[i]

                if n == 0 or n == N-1:
                    i += (2 * N - 2)
                else :
                    if f :
                        i += (2 * (N-n) -2)
                    else :
                        i += n*2
                    f ^= True

        return res
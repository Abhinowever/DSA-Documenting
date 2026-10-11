class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        curr = [["."] * n for _ in range(n)]

        result = []

        left = set()
        right = set()
        down = set() 
        def queens(x):
            if x == n :
                result.append(["".join(row) for row in curr])
                return

            for y in range(n):

                if y not in down and (x+y) not in left and (x-y) not in right :
                    curr[x][y] = "Q"
                    down.add(y)
                    left.add(x + y)
                    right.add(x - y)

                    queens(x+1)

                    curr[x][y] = "."
                    down.remove(y)
                    left.remove(x + y)
                    right.remove(x - y)

        queens(0)
        return result
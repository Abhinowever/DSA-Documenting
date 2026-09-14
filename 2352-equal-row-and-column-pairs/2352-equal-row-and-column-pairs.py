from collections import defaultdict
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        columns = Counter(
            tuple(grid[i][j] for i in range(n))
            for j in range(n))
        cnt = 0
        for row in grid:
            cnt += columns[tuple(row)]
        return cnt



        # for j in range(n):
        #     curr = []
        #     for i in range(n):
        #         curr.append(grid[i][j])
        #     row[grid[0][j]].append(curr)
        # # print(row)
        # for i in grid:
        #     t = i[0] 
        #     if t in row :
        #         for item in row[t] :
        #             if i == item :
        #                 cnt += 1
        # return cnt
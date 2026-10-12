class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        l,m = len(grid),len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(l)]
        islands = 0
        def dfs(i,j):
            visited[i][j] = True
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < l and 0 <= nj < m :
                    if grid[ni][nj] == '1' and not visited[ni][nj]:
                        dfs(ni, nj)

        for i in range(l):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j] :
                    dfs(i,j)
                    islands += 1

        return islands
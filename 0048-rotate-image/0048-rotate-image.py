class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # l = len(matrix)
        # b = len(matrix[0])
        # # new = [[0]*b]*l
        # # print(new)
        # new = [[0 for _ in range(l)] for _ in range(b)]
        # for i in range(l):
        #     for j in range(b):
        #         new[i][j] = matrix[b-j-1][i]
        # for i in range(l):
        #     for j in range(b):
        #         if matrix[i][j] != new[i][j]:
        #             matrix[i][j] = new[i][j]
        # print(new)

        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i < j :
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for element in matrix :
            element.reverse()
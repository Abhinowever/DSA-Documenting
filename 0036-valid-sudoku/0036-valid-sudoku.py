class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                i = board[r][c]
                if i == "." :
                    continue
                
                box = r//3 * 3 + c//3

                if (i in rows[r]) or ( i in columns[c] ) or ( i in boxes[box]) :
                    return False
                
                rows[r].add(i)
                columns[c].add(i)
                boxes[box].add(i)

        return True
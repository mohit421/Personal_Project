'''

'''

# Lees OPptmised


class Solution:

    def isValid(self, board, row, col , c):
        for i in range(9):
            if board[i][col] == c:
                return False
            if board[row][i] == c:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3] == c:
                return False
        return True

        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    for c in "123456789":
                        if self.isValid(board,i,j,c):
                            board[i][j] = c
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

        

# SOlution Recursive  optimised


from typing import List

class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # initialize sets and empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)

        def backtrack(idx=0):
            if idx == len(empties):
                return True
            i, j = empties[idx]
            b = (i // 3) * 3 + (j // 3)

            for c in "123456789":
                if c not in rows[i] and c not in cols[j] and c not in boxes[b]:
                    # place
                    board[i][j] = c
                    rows[i].add(c)
                    cols[j].add(c)
                    boxes[b].add(c)

                    if backtrack(idx + 1):
                        return True

                    # undo
                    board[i][j] = '.'
                    rows[i].remove(c)
                    cols[j].remove(c)
                    boxes[b].remove(c)

            return False

        backtrack(0)

'''

'''



# Solution 
'''
Time Complexity:  O(m*n*4^k), where “K” is the length of the word. And we are searching for the letter m*n times in the worst case. Here 4 in 4^k is because at each level of our decision tree we are making 4 recursive calls which equal 4^k in the worst case.

Space Complexity: O(K), Where k is the length of the given words
'''
class Solution:

    def wordSearch(self, board: List[List[str]], word: str, row:int, col:int, index: int, m:int, n:int):
        if index == len(word):
            return True
        if row < 0 or col < 0 or row == m or col == n or board[row][col] != word[index] or board[row][col] == "!":
            return False
        
        c = board[row][col]
        board[row][col] = "!"

        top = self.wordSearch(board,word, row-1, col, index+1, m,n)
        right = self.wordSearch(board,word, row, col+1, index+1, m,n)
        left = self.wordSearch(board,word, row, col-1, index+1, m,n)
        bottom = self.wordSearch(board,word, row+1, col, index+1, m,n)


        board[row][col] = c
        return top or right or left or bottom



    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        index = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[index]:
                    if self.wordSearch(board,word,i,j,index, m,n):
                        return True
        return False
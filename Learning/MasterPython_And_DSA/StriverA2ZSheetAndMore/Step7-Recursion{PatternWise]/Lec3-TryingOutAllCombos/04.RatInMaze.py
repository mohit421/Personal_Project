'''

'''

# Solution 
class Solution:
    # Function to find all possible paths
    def possiblePath(self, i, j, maze, res, st, n, m, vis):
        # If destination is reached
        if i == n-1 and j == m-1:
            res.append(st)
            return

        # Mark current cell visited
        vis[i][j] = 1

        # Downward
        if i+1 < n and not vis[i+1][j] and maze[i+1][j] == 1:
            self.possiblePath(i+1, j, maze, res, st+'D', n, m, vis)

        # Left
        if j-1 >= 0 and not vis[i][j-1] and maze[i][j-1] == 1:
            self.possiblePath(i, j-1, maze, res, st+'L', n, m, vis)

        # Right
        if j+1 < m and not vis[i][j+1] and maze[i][j+1] == 1:
            self.possiblePath(i, j+1, maze, res, st+'R', n, m, vis)

        # Upward
        if i-1 >= 0 and not vis[i-1][j] and maze[i-1][j] == 1:
            self.possiblePath(i-1, j, maze, res, st+'U', n, m, vis)

        # Unmark for backtracking
        vis[i][j] = 0

    def ratInMaze(self, maze):
        res = []
        n = len(maze)
        m = len(maze[0])  # safer than assuming square
        vis = [[0 for _ in range(m)] for _ in range(n)]
        
        if maze[0][0] == 1:
            self.possiblePath(0, 0, maze, res, "", n, m, vis)
        return res

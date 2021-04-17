# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    
    def dfs(self, grid, i, j, old_colour, new_colour):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != old_colour:
            return
        else:
            grid[i][j] = new_colour
            self.dfs(grid, i + 1, j, old_colour, new_colour)
            self.dfs(grid, i - 1, j, old_colour, new_colour)
            self.dfs(grid, i, j + 1, old_colour, new_colour)
            self.dfs(grid, i, j - 1, old_colour, new_colour)
    
    def fill(self, grid, i, j, new_colour):
        old_colour = grid[i][j]
        if old_colour == new_colour:
            return
        self.dfs(grid, i, j, old_colour, new_colour)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands += 1
                    self.fill(grid, i, j, '2')
        return islands
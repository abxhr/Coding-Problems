# Author: Abshar Mohammed Aslam, github: @abxhe

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        while k: 
            rowz = []
            rowL = len(grid[0])
            for i in range(len(grid)):
                rowz.append(grid[i][rowL-1])
                grid[i] = grid[i][0:-1]
            grid[0].insert(0,rowz[-1])
            for i in range(1,len(grid)):
                grid[i] = [rowz[i-1]] + grid[i]
            k-=1
        return grid

# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0 for _ in range(glasses)] for glasses in range(1,query_row+2)]
        tower[0][0] = poured

        for i in range(query_row):
            for j in range(len(tower[i])):
                glass_split = (tower[i][j] - 1)/2
                if glass_split>0:
                    tower[i+1][j] += glass_split
                    tower[i+1][j+1] += glass_split

        if tower[query_row][query_glass] > 1:
            return 1
        return tower[query_row][query_glass]
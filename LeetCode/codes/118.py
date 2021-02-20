# Author: Abdhar Mohammed Aslam, github.com/abxhr

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(numRows):
            newRow = []
            for i in range(row+1):
                if i == 0 or i == row:
                    newRow.append(1)
                else:
                    newRow.append(triangle[row-1][i-1] + triangle[row-1][i])
            triangle.append(newRow)
        return triangle
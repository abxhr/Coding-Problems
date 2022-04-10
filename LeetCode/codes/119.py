# Author: Abshar Mohammed Aslam, github: @abxhr

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for row in range(rowIndex+1):
            currRow = []
            for k in range(row+1):
                if k == 0 or k == row:
                    currRow.append(1)
                else:
                    currRow.append(triangle[row-1][k-1] + triangle[row-1][k])
            triangle.append(currRow)
        return triangle[rowIndex]

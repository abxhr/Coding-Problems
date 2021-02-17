# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        lst = []
        for i in range(n):
            val = []
            for j in range(m):
                val.append(0)
            lst.append(val)
        for ind in indices:
            for i in range(n):
                for j in range(m):
                    if i == ind[0]:
                        lst[i][j] += 1
                    if j == ind[1]:
                        lst[i][j] += 1
        c = 0
        for i in range(n):
            for j in range(m):
                if lst[i][j]%2 != 0:
                    c += 1
        return c
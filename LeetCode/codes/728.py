# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = []
        for i in range(left, right+1):
            f = True
            for j in str(i):
                if j == '0':
                    f = False
                    break
                elif i % int(j) != 0:
                    f = False
            if f:
                lst.append(i)
        return lst

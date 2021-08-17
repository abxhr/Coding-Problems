# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def sumZero(self, n: int) -> List[int]:
        lst = []
        for i in range(1, int(n/2)+1):
            lst.append(i)
            lst.append(-i)
        if (n % 2):
            lst.append(0)
        return lst

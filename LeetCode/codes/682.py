# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for x in ops:
            if x == '+':
                record.append(record[-1]+record[-2])
            elif x == 'D':
                record.append(record[-1]*2)
            elif x == 'C':
                record.pop()
            else:
                record.append(int(x))
        return sum(record)
